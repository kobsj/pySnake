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

#set up snake and controls

#apples

#scoring and score UI
