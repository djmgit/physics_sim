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
        (self.angle, self.speed) = addVectors(self.angle, self.speed, gravity[0], gravity[1])

        print (self.x)

    def bounce(self):
        if self.x > width - self.size:
            self.x = 2 * (width - self.size) - self.x
            self.angle = - self.angle
        elif self.x < self.size:
            self.x = 2 * self.size - self.x
            self.angle = - self.angle
        if self.y > height - self.size:
            self.y = 2 * (height - self.size) - self.y
            self.angle = math.pi - self.angle
        elif self.y < self.size:
            self.y = 2 * self.size - self.y
            self.angle = math.pi - self.angle



def addVectors(angle1, length1, angle2, length2):
    x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y  = math.cos(angle1) * length1 + math.cos(angle2) * length2

    length = math.hypot(x, y)
    angle = 0.5 * math.pi - math.atan2(y, x)
    return (angle, length)

background_colour = (255,255,255)
gravity = (math.pi, 0.002)
(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')


number_of_particles = 10
my_particles = []
for n in range(number_of_particles):
    size = random.randint(10, 20)
    x = random.randint(size, width-size)
    y = random.randint(size, height-size)
    particle = Particle(x, y, size)
    particle.speed = random.random()
    particle.angle = random.uniform(0, math.pi*2)
    my_particles.append(particle)



running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  screen.fill(background_colour)
  for particle in my_particles:
    particle.move()
    particle.bounce()
    particle.display()

  pygame.display.flip()
  

