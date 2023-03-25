#Create a simple clock application (only with minutes and seconds) which is synchronized with system clock.
#Use Mickey's right hand as minutes arrow and left - as seconds.
import datetime
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((830, 900))
sec = pygame.image.load("minute.png")
min = pygame.image.load("second.png")
back = pygame.image.load("mickeyclock.jpeg")
pygame.display.set_caption("hickey clock")
sec2 = pygame.transform.scale(sec, (200, 200))
min2 = pygame.transform.scale(min, (200, 200))
clock = pygame.time.Clock()

def transformed(surface, image, topleft, angle):
    rotated = pygame.transform.rotate(image, angle)
    rectg = rotated.get_rect(center = image.get_rect(topleft = topleft).center)
    surface.blit(rotated, rectg)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(back, (0, 0))
    time = datetime.datetime.now()
    minute = time.minute
    second = time.second   
    transformed(screen, sec2, (370, 248), second* -6)
    transformed(screen, min2, (370, 248), minute* -6)
    pygame.display.flip()
    clock.tick(60)