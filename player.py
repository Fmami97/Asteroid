from circleshape import CircleShape
from constants import *
from shot import Shot
import pygame
class Player(CircleShape):
    containers = None

    def __init__(self,x:int,y:int):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def shoot(self):
        if(self.cooldown > 0):
            return
        new_shot = Shot(self.position[0],self.position[1],SHOT_RADIUS)
        new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)*PLAYER_SHOOT_SPEED
        self.cooldown = PLAYER_SHOOT_COOLDOWN
    def draw(self, screen):
        pygame.draw.polygon(screen,(255,255,255),self.triangle(),2)

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def rotate(self,dt):
        self.rotation += dt * PLAYER_TURN_SPEED

    def update(self, dt):
        if self.cooldown > 0:
            self.cooldown -= dt
        if self.cooldown < 0:
            self.cooldown = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt*-1)
        if keys[pygame.K_a]:
            self.rotate(dt*-1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        