import pygame
from pygame.color import THECOLORS
from pygame.draw import *

pygame.init()

FPS = 40
screen = pygame.display.set_mode((400, 400))
screen.fill(THECOLORS['grey'])

pygame.draw.circle(screen, THECOLORS['yellow'], (200, 200), 100) #КРУГ ЖЁЛТЫЙ ВЕСЬ
pygame.draw.circle(screen, THECOLORS['black'], (200,200), 100, 2) #КРУГ ОБВОДКА ЧЕРНАЯ

pygame.draw.rect(screen, THECOLORS['black'], (150,240,102,22)) #

pygame.draw.circle(screen, THECOLORS['red'], (154, 170), 20) #
pygame.draw.circle(screen, THECOLORS['black'], (154,170), 20, 2) #
pygame.draw.circle(screen, THECOLORS['black'], (154,170), 8) #

pygame.draw.circle(screen, THECOLORS['red'], (250,170), 16)
pygame.draw.circle(screen, THECOLORS['black'], (250,170), 16, 2)
pygame.draw.circle(screen, THECOLORS['black'], (250,170), 7)

pygame.draw.polygon(screen, THECOLORS['black'], ((110, 140), (200,170), (200,160), (110,130)))
pygame.draw.polygon(screen, THECOLORS['black'], ((220, 160), (225,170), (335,100), (330,90)))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
