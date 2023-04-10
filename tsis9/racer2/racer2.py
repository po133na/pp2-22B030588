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
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0
coin_num = 0
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
 
background = pygame.image.load("AnimatedStreet.png")
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

#Diff coins for bonuses
class Coin25(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("25.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0, 10)
        

class Coin50(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("50.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0, 10)

class Coin75(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("75.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0, 10)

#class 'Enemy'
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
#class 'Player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                   
#creating characters       
P1 = Player()
E1 = Enemy()
coin25 = Coin25()
coin50 = Coin50()
coin75 = Coin75()
 
#Sprites group
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(coin25, coin50, coin75)
coin_group = pygame.sprite.Group()
coin_group.add(coin25, coin50, coin75)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
COIN25_SPAWN = pygame.USEREVENT + 2
pygame.time.set_timer(COIN25_SPAWN, 3000)
COIN50_SPAWN = pygame.USEREVENT + 3
pygame.time.set_timer(COIN50_SPAWN, 7500)
COIN75_SPAWN = pygame.USEREVENT + 4
pygame.time.set_timer(COIN75_SPAWN, 12500)

#Game Loop
while True:
       
    #all occurring events
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == COIN25_SPAWN:
            coin25.rect.top = 0
            coin25.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        if event.type == COIN50_SPAWN:
            coin50.rect.top = 0
            coin50.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        if event.type == COIN75_SPAWN:
            coin75.rect.top = 0
            coin75.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

 
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    coin_scores = font_small.render( 'Coins: ' + str(COIN_SCORE) , True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coin_scores, (285, 10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    #To be run if collision occurs between Player and coins
    if pygame.sprite.collide_rect(P1, coin25):
        COIN_SCORE += 25
        coin25.rect.top = 0
        coin25.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    if pygame.sprite.collide_rect(P1, coin50):
        COIN_SCORE += 50
        coin50.rect.top = 0
        coin50.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    if pygame.sprite.collide_rect(P1, coin75):
        COIN_SCORE += 75
        coin75.rect.top = 0
        coin75.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    if pygame.sprite.spritecollideany(P1, coin_group):
        coin_num +=1
        if coin_num % 5 == 0:
            SPEED += 5


    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)