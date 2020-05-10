import pygame
import sys
import random
import time

#error check

check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized!")

#play surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snakey')

red = pygame.Color(255, 0, 0) #gameover
green = pygame.Color(0, 255, 0) #snake
blue = pygame.Color(0, 0, 255) # Food
black = pygame.Color(0, 0, 0) #score
white = pygame.Color(255, 255, 255) #background

fpsController = pygame.time.Clock()

snakePos = [360, 230]
snakeBody = [[360, 230], [350, 230], [340, 230]]

foodPos = [random.randrange(1, 72)*10, random.randrange(1, 46)*10]
foodSpawn = True

direction = 'RIGHT'
changeTo = direction

#Game over
def GameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    goSurface = myFont.render('GAME OVER', True, red)
    goRect = goSurface.get_rect()
    goRect.midtop = (360, 15)
    playSurface.blit(goSurface, goRect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

#Controls
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeTo = 'RIGHT'
            if event.key == pygame.K_RIGHT or event.key == ord('a'):
                changeTo = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('w'):
                changeTo = 'UP'
            if event.key == pygame.K_RIGHT or event.key == ord('s'):
                changeTo = 'DOWN'
            if event.key ++ pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
