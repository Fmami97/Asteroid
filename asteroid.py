from circleshape import CircleShape
from constants import *
import random
import pygame
class Asteroid(CircleShape):
    containers = None
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0,0)
    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius,2)
    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):    
        if(self.radius > ASTEROID_MIN_RADIUS):
            random_angle = random.uniform(20,50)
            point1 = self.velocity.rotate(random_angle)
            point2 = self.velocity.rotate(random_angle*-1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position[0],self.position[1],new_radius)
            a1.velocity = point1 * 1.2
            a2 = Asteroid(self.position[0],self.position[1],new_radius)
            a2.velocity = point2* 1.2
        self.kill()
