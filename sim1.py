import pygame
import random
import math

class Particle:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = (0, 0, 255)
        self.thickness = 1
        self.speed = 0.01
        self.angle = math.pi / 2

    def display(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size, self.thickness)

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

        print (self.x)


background_colour = (255,255,255)
(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')


number_of_particles = 10
my_particles = []
for n in range(number_of_particles):
    size = random.randint(10, 20)
    x = random.randint(size, width-size)
    y = random.randint(size, height-size)
    my_particles.append(Particle(x, y, size))



running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  screen.fill(background_colour)
  for particle in my_particles:
    particle.move()
    particle.display()

  pygame.display.flip()
  

