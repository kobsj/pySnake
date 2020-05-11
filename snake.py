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
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeTo = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeTo = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeTo = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    if changeTo == 'RIGHT' and direction != 'LEFT': #if fail use not direction
        direction = 'RIGHT'
    if changeTo == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if changeTo == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if changeTo == 'DOWN' and direction != 'UP':
        direction = 'DOWN'

    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        foodSpawn = False
    else:
        snakeBody.pop()

    if foodSpawn == False:
        foodPos = [random.randrange(1, 72)*10, random.randrange(1, 46)*10]
        foodSpawn = True

    playSurface.fill(white)

    for pos in snakeBody:
        pygame.draw.rect(playSurface, green,
        pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(playSurface, blue,
    pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    if snakePos[0] > 720 or snakePos[0] < 0 or snakePos[1] > 460 or snakePos[1] < 0:
        GameOver()

    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            GameOver()

    pygame.display.flip()
    fpsController.tick(20)
