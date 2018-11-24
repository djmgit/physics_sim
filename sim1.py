import pygame
import random
import math


background_colour = (255,255,255)
gravity = (math.pi, 0.002)
drag = 0.999
elasticity = 0.75
mass_of_air = 0.2
(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Physics simulation')


number_of_particles = 3
my_particles = []
for n in range(number_of_particles):
    size = random.randint(10, 20)
    density = random.randint(1, 20)
    x = random.randint(size, width-size)
    y = random.randint(size, height-size)
    particle = Particle(x, y, size, density * size ** 2)
    particle.background_colour = (200 - density * 10, 200 - density * 10, 255)
    particle.speed = random.random()
    particle.angle = random.uniform(0, math.pi*2)
    my_particles.append(particle)



running = True
selected_particle = None
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        (mouseX, mouseY) = pygame.mouse.get_pos()
        print (mouseX, mouseY)
        selected_particle = findParticle(my_particles, mouseX, mouseY)
        print (selected_particle)
        if selected_particle:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            dx = mouseX - selected_particle.x
            dy = mouseY - selected_particle.y
            selected_particle.angle = math.atan2(dy, dx) + 0.5*math.pi
            selected_particle.speed = math.hypot(dx, dy) * 0.1
    elif event.type == pygame.MOUSEBUTTONUP:
        selected_particle = None

  screen.fill(background_colour)

  for i, particle in enumerate(my_particles):
      particle.move()
      particle.bounce()
      for particle2 in my_particles[i+1:]:
          collide(particle, particle2)
      particle.display()

  pygame.display.flip()
  

