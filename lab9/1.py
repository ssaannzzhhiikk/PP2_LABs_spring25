#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
 
#Other Variables for use in the program
coin_collide = False
coin_collide5 = False
coin_collide10 = False
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load(r"lab9\racer_materials\animatedStreet.png")
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

#Coin 1
class Coin1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(r"lab9\racer_materials\coin1.png"), (60,60))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
    def move(self):
        global COIN_SCORE
        global coin_collide
        self.rect.move_ip(0, 7)
        if (coin_collide): #Adds 1 if coin collides
            COIN_SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            coin_collide = False
        if (self.rect.top > 600): #Respawns if coin reached border
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            coin_collide = False

 
class Coin5(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(r"lab9\racer_materials\coin5.png"), (60,60))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
    def move(self):
        global COIN_SCORE
        global coin_collide5
        self.rect.move_ip(0, 3)
        if (coin_collide5): #Adds 5 if coin is collided
            COIN_SCORE += 5
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            coin_collide5 = False
        if(self.rect.top > 600): #Respawns if coin reached border
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            coin_collide5 = False


class Coin10(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(r"lab9\racer_materials\coin10.png"), (60,60))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
    def move(self):
        global COIN_SCORE
        global coin_collide10
        self.rect.move_ip(0, 2) #Speed 2
        if (coin_collide10): #Ads 10 if collided
            COIN_SCORE += 10
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            coin_collide10 = False
        if (self.rect.top > 600): #Respawns coin if it reaches border
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            coin_collide10 = False


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"lab9\racer_materials\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"lab9\racer_materials\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 500)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)


#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin1()
C5 = Coin5()
C10 = Coin10()


#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)
coins.add(C5)
coins.add(C10)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(C5)
all_sprites.add(C10)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

INC_SPEED_COIN = pygame.USEREVENT + 1

#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == INC_SPEED_COIN:
            SPEED += 1
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    #Displays score and coin score
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    coin_scores = font_small.render(str(COIN_SCORE), True, YELLOW)
    DISPLAYSURF.blit(coin_scores, (10,30))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound(r"lab9\racer_materials\crash.wav").play()
          time.sleep(0.5)
          total_score = font_small.render(f"Your score is: {str(COIN_SCORE)}", True, BLACK)      
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          DISPLAYSURF.blit(total_score, (30, 330))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()   

    if P1.rect.colliderect(C1.rect):
        coin_collide = True
    
    if P1.rect.colliderect(C5.rect):
        coin_collide5 = True

    if P1.rect.colliderect(C10.rect):
        coin_collide10 = True
    
    if COIN_SCORE > 9 and COIN_SCORE % 10 == 0:
        pygame.event.post(pygame.event.Event(INC_SPEED_COIN))

    pygame.display.update()
    FramePerSec.tick(FPS)