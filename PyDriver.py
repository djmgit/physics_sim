import pygame
import PyParticles
pygame.display.set_caption('Tutorial 10')
(width, height) = (400, 400)
screen = pygame.display.set_mode((width, height))

env = PyParticles.Environment(width, height)
env.addParticles(5)

running = True
while running:
    selected_particle = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            selected_particle = env.findParticle(mouse_pos[0], mouse_pos[1])
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_particle = None

    if selected_particle:
        mouse_pos = pygame.mouse.get_pos()
        selected_particle.mouseMove(mouse_pos[0], mouse_pos[1])

    screen.fill(env.colour)
    for p in env.particles:
        pygame.draw.circle(screen, p.colour, (int(p.x), int(p.y)), p.size)

    env.update()
    pygame.display.flip()

