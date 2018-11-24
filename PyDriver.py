import pygame
import PyParticles
pygame.display.set_caption('Tutorial 10')
(width, height) = (400, 400)
screen = pygame.display.set_mode((width, height))

env = PyParticles.Environment(width, height)
env.addParticles(5)
screen.fill(env.colour)
for p in env.particles:
    pygame.draw.circle(screen, p.colour, (int(p.x), int(p.y)), p.size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

