#Draw circle - a red ball of size 50 x 50 (radius = 25) on white background. 
#When user presses Up, Down, Left, Right arrow keys on keyboard, 
#the ball should move by 20 pixels in the direction of pressed key. 
#The ball should not leave the screen, i.e. 
#user input that leads the ball to leave of the screen should be ignored
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("circle")
r = 25
x, y = 500, 500
cond = False
clock = pygame.time.Clock()
while not cond:
    clock.tick(60)
    for cycle in pygame.event.get():
        if cycle.type == pygame.QUIT:
            cond = True

    butts = pygame.key.get_pressed()
    if butts[pygame.K_UP] and y-r > 0:
        y += -20
    elif butts[pygame.K_DOWN] and y+r < 600:
        y += 20
    elif butts[pygame.K_RIGHT] and x+r < 800:
        x += 20
    elif butts[pygame.K_LEFT] and x-r > 0:
        x += -20
        
    screen.fill("#FFFFFF")
    pygame.draw.circle(screen, "#FF0000", (x, y), r)
    
    pygame.display.flip()
pygame.quit()
sys.quit()