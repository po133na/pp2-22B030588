#Create music player with keyboard controller. You have to be able to press keyboard:
#play, stop, next and previous as some keys. Player has to react to the given command appropriately.
import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("nice pleasing music")

playlist = ['tenebro.mp3', 'cataclysm.mp3']

pygame.mixer.init()
pygame.mixer.music.load(playlist[0])
#keyboardd
play_key = pygame.K_RETURN
stop_key = pygame.K_SPACE
next_key = pygame.K_RIGHT
prev_key = pygame.K_LEFT

current_track = 0

def play():
    pygame.mixer.music.play()
def pause():
    pygame.mixer.music.pause()
def stop():
    pygame.mixer.music.stop()
def next():
    global current_track
    if current_track < len(playlist) - 1:
        current_track += 1
        pygame.mixer.music.load(playlist[current_track])
        pygame.mixer.music.play()
def previous():
    global current_track
    if current_track > 0:
        current_track -= 1
        pygame.mixer.music.load(playlist[current_track])
        pygame.mixer.music.play()

background = pygame.image.load("coole.png")
while True:
    screen.blit(background, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == play_key:
                play()
            elif event.key == stop_key:
                stop()
            elif event.key == next_key:
                next()
            elif event.key == prev_key:
                previous()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()