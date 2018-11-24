import random
import math

class Particle:
    def __init__(self, x, y, size, mass=1):
        self.x = x
        self.y = y
        self.size = size
        self.color = (0, 0, 255)
        self.thickness = 1
        self.speed = 0.01
        self.angle = math.pi / 2
        self.mass = mass
        self.mass_of_air = 0.2
        self.drag = (self.mass/(self.mass + self.mass_of_air)) ** self.size
        self.elasticity = 0.9

    #def display(self):
        #pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        #(self.angle, self.speed) = addVectors(self.angle, self.speed, gravity[0], gravity[1])
        self.speed *= self.drag

        #print (self.x)

    def mouseMove(self, x, y):
        dx = x - self.x
        dy = y - self.y
        self.angle = 0.5*math.pi + math.atan2(dy, dx)
        self.speed = math.hypot(dx, dy) * 0.1

def addVectors(angle1, length1, angle2, length2):
    x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y  = math.cos(angle1) * length1 + math.cos(angle2) * length2

    length = math.hypot(x, y)
    angle = 0.5 * math.pi - math.atan2(y, x)
    return (angle, length)

def collide(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y        
    distance = math.hypot(dx, dy)

    if distance < p1.size + p2.size:
       angle = math.atan2(dy, dx) + 0.5 * math.pi
       total_mass = p1.mass + p2.mass
       (p1.angle, p1.speed) = addVectors(p1.angle, p1.speed*(p1.mass-p2.mass)/total_mass, angle, 2*p2.speed*p2.mass/total_mass)
       (p2.angle, p2.speed) = addVectors(p2.angle, p2.speed*(p2.mass-p1.mass)/total_mass, angle+math.pi, 2*p1.speed*p1.mass/total_mass)
       


       elasticity = p1.elasticity * p2.elasticity
       p1.speed *= elasticity
       p2.speed *= elasticity

       overlap = 0.5 * (p1.size + p2.size - distance + 1)
       p1.x += math.sin(angle) * overlap
       p1.y -= math.cos(angle) * overlap
       p2.x -= math.sin(angle) * overlap
       p2.y += math.cos(angle) * overlap

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.particles = []
        self.colour = (255,255,255)
        self.mass_of_air = 0.2
        self.elasticity = 0.75

    def addParticles(self, n=1, **kargs):
      for i in range(n):
        size = kargs.get('size', random.randint(10, 20))
        mass = kargs.get('mass', random.randint(100, 10000))
        x = kargs.get('x', random.uniform(size, self.width-size))
        y = kargs.get('y', random.uniform(size, self.height-size))
        p = Particle(x, y, size, mass)
        p.speed = kargs.get('speed', random.random())
        p.angle = kargs.get('angle', random.uniform(0, math.pi*2))
        p.colour = kargs.get('colour', (0, 0, 255))
        p.drag = (p.mass/(p.mass + self.mass_of_air)) ** p.size
        self.particles.append(p)

    def bounce(self, particle):
        if particle.x > self.width - particle.size:
            particle.x = 2 * (self.width - particle.size) - particle.x
            particle.angle = - particle.angle
            particle.speed *= self.elasticity
        elif particle.x < particle.size:
            particle.x = 2 * particle.size - particle.x
            particle.angle = - particle.angle
            particle.speed *= self.elasticity
        if particle.y > self.height - particle.size:
            particle.y = 2 * (self.height - particle.size) - particle.y
            particle.angle = math.pi - particle.angle
            particle.speed *= self.elasticity
        elif particle.y < particle.size:
            particle.y = 2 * particle.size - particle.y
            particle.angle = math.pi - particle.angle
            particle.speed *= self.elasticity


    def update(self):
        for i, particle in enumerate(self.particles):
            particle.move()
            self.bounce(particle)
            for particle2 in self.particles[i+1:]:
                collide(particle, particle2)

    def findParticle(self, x, y):
        for p in self.particles:
            if math.hypot(p.x-x, p.y-y) <= p.size:
                return p
        return None

