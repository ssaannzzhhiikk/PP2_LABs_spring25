import pygame, sys, random
import psycopg2
from pygame.locals import *

pygame.init()

#database part
def connect():
    return psycopg2.connect(
        host="localhost",
        database="snake",
        user="postgres",
        password="Albatros2143"
    )

def create_tables():
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL
        );
    """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_scores (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            score INTEGER NOT NULL,
            level INTEGER NOT NULL,
            saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    conn.commit()
    cur.close()
    conn.close()

def get_or_create_user(username):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    result = cur.fetchone()
    
    if result:
        user_id = result[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()

    cur.close()
    conn.close()
    return user_id

def get_user_last_score(user_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT score, level FROM user_scores 
        WHERE user_id = %s 
        ORDER BY saved_at DESC 
        LIMIT 1
    """, (user_id,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result  # (score, level) or None

def save_score(user_id, score, level):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO user_scores (user_id, score, level) 
        VALUES (%s, %s, %s)
    """, (user_id, score, level))
    conn.commit()
    cur.close()
    conn.close()

#Game variables
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

SPEED = 15  
SNAKE_WIDTH = 30 
INITIAL_DELAY = 100
food_size = 15  
FONT = pygame.font.Font(None, 36)
font = pygame.font.Font(None, 48)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

#Class Snake
class Snake:
    def __init__(self, x, y):
        self.body = [pygame.Rect(x, y, SNAKE_WIDTH, SNAKE_WIDTH)]
        self.food = self.generate_food()
        self.food2 = self.special_food()
        self.dx, self.dy = SPEED, 0
        self.last_level_score = 0
        self.last_dx, self.last_dy = self.dx, self.dy
        self.score = 0
        self.level = 1
        self.delay = INITIAL_DELAY
        self.weight = random.randint(1, 5)
        self.rand_color = (0, 0, self.weight*51)

    def generate_food(self):
        while True:
            new_rect = pygame.Rect(
                random.randint(0, WIDTH // SPEED - 1) * SPEED-1,
                random.randint(0, HEIGHT // SPEED - 1) * SPEED-1,
                food_size, food_size
            )
            if all(not segment.colliderect(new_rect) for segment in self.body):
                return new_rect
    
    def special_food(self):
        while True:    
            spec_rect = pygame.Rect(
                random.randint(0, WIDTH // SPEED - 1) * SPEED-1,
                random.randint(0, HEIGHT // SPEED - 1) * SPEED-1,
                food_size, food_size
            )
            if all(not segment.colliderect(spec_rect) for segment in self.body) and not spec_rect.colliderect(self.food):
                return spec_rect

    def update(self):
        new_head = self.body[0].copy()
        new_head.move_ip(self.dx, self.dy)

        if new_head.left < 0 or new_head.right > WIDTH or new_head.top < 0 or new_head.bottom > HEIGHT or new_head in self.body:
            pygame.quit()
            sys.exit()

        self.body.insert(0, new_head)

        eaten = False
        global drawn
        if new_head.colliderect(self.food2):
            self.food2 = self.special_food()
            self.score += 8
            drawn = False
            eaten = True

        if new_head.colliderect(self.food):
            self.food = self.generate_food()
            self.score += self.weight
            self.weight = random.randint(1, 5)
            self.rand_color = (0, 0, self.weight*51)
            eaten = True

        if not eaten:
            self.body.pop()

        if self.score - self.last_level_score >= 5:
            self.level += 1
            self.last_level_score = self.score
            self.delay = max(50, self.delay - 20)

        self.last_dx, self.last_dy = self.dx, self.dy

    def change_direction(self, dx, dy):
        if (dx, dy) != (-self.last_dx, -self.last_dy):
            self.dx, self.dy = dx, dy

    def draw(self, surface):
        global drawn
        for segment in self.body:
            pygame.draw.rect(surface, RED, segment)
        pygame.draw.rect(surface, self.rand_color, self.food)
        if drawn:
            pygame.draw.rect(surface, YELLOW, self.food2)

        score_text = FONT.render(f"Score: {self.score}  Level: {self.level}", True, BLACK)
        surface.blit(score_text, (10, 10))

#Game Loop
create_tables()
player = Snake(200, 200)

input_text = ""
active = True
typed = False
drawn = False
paused = False
current_user_id = None

PERM_FOOD = pygame.USEREVENT + 1
pygame.time.set_timer(PERM_FOOD, 6000)

while True:
    if not paused:
        pygame.time.delay(player.delay)

    for event in pygame.event.get():
        if event.type == PERM_FOOD:
            drawn = not drawn
            if drawn:
                player.food2 = player.special_food()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if not typed:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    current_user_id = get_or_create_user(input_text)
                    last = get_user_last_score(current_user_id)
                    if last:
                        player.score, player.level = last
                        player.delay = max(50, INITIAL_DELAY - (player.level - 1) * 20)
                    typed = True
                else:
                    input_text += event.unicode
            else:
                if event.key == pygame.K_p:
                    paused = not paused
                    if paused:
                        save_score(current_user_id, player.score, player.level)

    if not typed:
        screen.fill((30, 30, 30))
        text_surface = font.render(f"Name: {input_text}", True, WHITE)
        screen.blit(text_surface, (50, 200))
        pygame.display.flip()
    elif not paused:
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]: player.change_direction(-SPEED, 0)
        if keys[K_RIGHT]: player.change_direction(SPEED, 0)
        if keys[K_UP]: player.change_direction(0, -SPEED)
        if keys[K_DOWN]: player.change_direction(0, SPEED)

        screen.fill(WHITE)
        player.draw(screen)
        player.update()
        pygame.display.flip()
    else:
        pause_text = font.render("Paused", True, BLACK)
        screen.fill((200, 200, 200))
        screen.blit(pause_text, (50, 200))
        pygame.display.flip()
