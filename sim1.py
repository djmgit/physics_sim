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
        self.speed *= drag

        #print (self.x)

    def bounce(self):
        if self.x > width - self.size:
            self.x = 2 * (width - self.size) - self.x
            self.angle = - self.angle
            self.speed *= elasticity
        elif self.x < self.size:
            self.x = 2 * self.size - self.x
            self.angle = - self.angle
            self.speed *= elasticity
        if self.y > height - self.size:
            self.y = 2 * (height - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity
        elif self.y < self.size:
            self.y = 2 * self.size - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity



def addVectors(angle1, length1, angle2, length2):
    x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y  = math.cos(angle1) * length1 + math.cos(angle2) * length2

    length = math.hypot(x, y)
    angle = 0.5 * math.pi - math.atan2(y, x)
    return (angle, length)

def findParticle(particles, x, y):
    for p in particles:
        if math.hypot(p.x-x, p.y-y) <= p.size:
            return p
    return None

def collide(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y        
    distance = math.hypot(dx, dy)

    if distance < p1.size + p2.size:
        tangent = math.atan2(dy, dx)

        p1.angle = 2 * tangent - p1.angle
        p2.angle = 2 * tangent - p2.angle
    
        (p1.speed, p2.speed) = (p2.speed, p1.speed)
    
        angle = 0.5 * math.pi + tangent
        p1.x += math.sin(angle)
        p1.y -= math.cos(angle)
        p2.x -= math.sin(angle)
        p2.y += math.cos(angle)
    
        p1.speed *= elasticity
        p2.speed *= elasticity

background_colour = (255,255,255)
gravity = (math.pi, 0.002)
drag = 0.999
elasticity = 0.75
(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Physics simulation')


number_of_particles = 3
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
  

