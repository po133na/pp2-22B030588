#Create a simple clock application (only with minutes and seconds) which is synchronized with system clock.
#Use Mickey's right hand as minutes arrow and left - as seconds.
import datetime
import pygame
import os

pygame.init()
screen = pygame.display.set_mode((1400, 1050))
time = datetime.datetime.now()
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()
#background
back = pygame.image.load('mickeyclock.png')
sec = pygame.image.load('min.png')
min = pygame.image.load('hour.png')

#game loop
run = True
while run:
    for cycle in pygame.event.get():
        if cycle.type == pygame.QUIT:
            run = False
            pygame.quit()
    screen.fill((0, 0, 0))
    #back images
    screen.blit(back, (0, 0))
    screen.c
pygame.display.flip()
