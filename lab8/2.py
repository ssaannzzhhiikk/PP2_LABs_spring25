import pygame, sys, random
from pygame.locals import *

pygame.init()

# Параметры окна
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Начальные параметры
SPEED = 20  
SNAKE_WIDTH = 30 
INITIAL_DELAY = 100
food_size = 15  
FONT = pygame.font.Font(None, 36)  

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

class Snake:
    def __init__(self, x, y):
        self.body = [pygame.Rect(x, y, SNAKE_WIDTH, SNAKE_WIDTH)]
        self.food = self.generate_food()
        self.dx, self.dy = SPEED, 0
        self.last_dx, self.last_dy = self.dx, self.dy
        self.score = 0
        self.level = 1
        self.delay = INITIAL_DELAY

    def generate_food(self):
        while True:
            new_rect = pygame.Rect(
                random.randint(0, WIDTH // SPEED - 1) * SPEED,
                random.randint(0, HEIGHT // SPEED - 1) * SPEED,
                food_size, food_size
            )
            if all(not segment.colliderect(new_rect) for segment in self.body):
                return new_rect

    def update(self):
        new_head = self.body[0].copy()
        new_head.move_ip(self.dx, self.dy)

        # Проверка столкновения с границей
        if new_head.left < 0 or new_head.right > WIDTH or new_head.top < 0 or new_head.bottom > HEIGHT:
            pygame.quit()
            sys.exit()

        # Проверка столкновения с собой
        if new_head in self.body:
            pygame.quit()
            sys.exit()

        self.body.insert(0, new_head)

        # Если не съели еду, удаляем хвост
        if not new_head.colliderect(self.food):
            self.body.pop()
        else:
            self.food = self.generate_food()
            self.score += 1

            # Уровень увеличивается каждые 3 еды
            if self.score % 3 == 0:
                self.level += 1
                self.delay = max(50, self.delay - 20)  # Уменьшаем задержку

        self.last_dx, self.last_dy = self.dx, self.dy

    def change_direction(self, dx, dy):
        if (dx, dy) != (-self.last_dx, -self.last_dy):
            self.dx, self.dy = dx, dy

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, RED, segment)
        pygame.draw.rect(surface, GREEN, self.food)

        # Отображение счета и уровня
        score_text = FONT.render(f"Score: {self.score}  Level: {self.level}", True, BLACK)
        surface.blit(score_text, (10, 10))


# Создаем объект змейки
player = Snake(200, 200)

while True:
    pygame.time.delay(player.delay)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Управление направлением
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        player.change_direction(-SPEED, 0)
    if keys[K_RIGHT]:
        player.change_direction(SPEED, 0)
    if keys[K_UP]:
        player.change_direction(0, -SPEED)
    if keys[K_DOWN]:
        player.change_direction(0, SPEED)

    # Обновление положения змейки
    player.update()

    # Отрисовка
    screen.fill(WHITE)
    player.draw(screen)
    pygame.display.flip()

pygame.quit()
