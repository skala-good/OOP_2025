import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

screen.fill((20, 20, 20))

rect(screen, (180, 180, 180), (0, 0, 400, 175))

circle(screen, (250, 250, 250), (350, 50), 40)

ellipse(screen, (50, 50, 50), (50, 50, 200, 30))
ellipse(screen, (90, 90, 90), (150, 70, 200, 30))
ellipse(screen, (150, 150, 150), (100, 30, 200, 30))
ellipse(screen, (120, 120, 120), (160, 30, 200, 30))

polygon(screen, (0, 0, 0), [(0, 150), (20, 120), (180, 120), (200, 150)])

rect(screen, (80, 80, 80), (140, 90, 10, 35))
rect(screen, (80, 80, 80), (60, 90, 10, 35))
rect(screen, (80, 80, 80), (165, 105, 10, 30))
rect(screen, (80, 80, 80), (100, 100, 18, 45))

rect(screen, (50, 50, 10), (20, 150, 160, 160))
rect(screen, (50, 50, 50), (0, 230, 200, 20))

rect(screen, (150, 150, 30), (70, 150, 20, 80))
rect(screen, (150, 150, 30), (30, 150, 20, 80))
rect(screen, (150, 150, 30), (110, 150, 20, 80))
rect(screen, (150, 150, 30), (150, 150, 20, 80))



rect(screen, (50, 50, 50), (10, 200, 180, 10))
rect(screen, (50, 50, 50), (155, 200, 15, 30))
rect(screen, (50, 50, 50), (125, 200, 15, 30))
rect(screen, (50, 50, 50), (85, 200, 15, 30))
rect(screen, (50, 50, 50), (55, 200, 15, 30))
rect(screen, (50, 50, 50), (30, 200, 15, 30))
rect(screen, (50, 50, 50), (5, 200, 5, 35))
rect(screen, (50, 50, 50), (185, 200, 5, 35))



Z = 300
ellipse(screen, (200, 200, 200), (300, 270, 90, 170))
for i in range(10):
    ellipse(screen, (20, 20, 20), (Z, 370, 20, 50))
    Z += 17

circle(screen, (0, 0, 0), (325, 300), 5)
circle(screen, (0, 0, 0), (355, 300), 5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()