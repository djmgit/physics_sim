import pygame
import PyParticles
pygame.display.set_caption('Tutorial 10')
(width, height) = (400, 400)
screen = pygame.display.set_mode((width, height))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

