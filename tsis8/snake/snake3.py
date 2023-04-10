import pygame
import time
import random
 
snake_speed = 15
WIDTH = 720
HEIGHT = 480
#colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()
pygame.display.set_caption('super snake!!!!!')
game_window = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.mixer.music.load('cataclysm.mp3')
background = pygame.mixer.music.play(-1)
#FPS controller
fps = pygame.time.Clock()
#snake default pos
snake_position = [100, 50]
 
#first 4 blocks of snake's body
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
#fruit pos
fruit_position = [random.randrange(1, (WIDTH//10)) * 10,
                  random.randrange(1, (HEIGHT//10)) * 10]
fruit_spawn = True #default food spawning 
#default snake direction
direction = 'RIGHT'
change_to = direction

score = 0
 #show score obvi
def show_score(choice, color, font, size):
    #creating where score will be displayed
    score_font = pygame.font.SysFont(font, size)
    #create the display surface object
    score_surface = score_font.render('Score : ' + str(score), True, color)
    #rect for score
    score_rect = score_surface.get_rect()
    #text
    game_window.blit(score_surface, score_rect)
#if we lose game
def game_over():
    pygame.display.flip()
    #quit after 2secs
    time.sleep(2)
    pygame.quit()
    quit()

#game loop
while True:
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
    #giving commands 2move
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 
    #collision while eating fruit
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (WIDTH//10)) * 10,
                          random.randrange(1, (HEIGHT//10)) * 10]
         
    fruit_spawn = True
    game_window.fill(black)
     
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(
          pos[0], pos[1], 10, 10))
         
    pygame.draw.rect(game_window, white, pygame.Rect(
      fruit_position[0], fruit_position[1], 10, 10))
 
    #if snake collides w// screen's ending
    if snake_position[0] < 0 or snake_position[0] > WIDTH-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > HEIGHT-10:
        game_over()
     
    #if snake touches its body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    #score displayed
    show_score(1, white, 'times new roman', 20)
     
    #updating game screen
    pygame.display.update()
    #rate of screen update
    fps.tick(snake_speed)

