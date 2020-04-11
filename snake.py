import pygame
import sys
import random
import time

#create window

check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized!")


#set up snake and controls

#apples

#scoring and score UI
