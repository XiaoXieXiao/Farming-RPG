import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.image = pygame.Surface((32,64))
        self.image.fill('green')
        self.rect = self.image.get_rect(center = pos)

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 150

    def input(self):
        keys = pygame.key.get_pressed()

        # direction input y axis
        if keys[pygame.K_w]:
            print('UP')
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
            print('DOWN')
        else:
            self.direction.y = 0
            print('STOP (Y)')

        # direction input x axis
        if keys[pygame.K_a]:
            self.direction.x = -1
            print('LEFT')
        elif keys[pygame.K_d]:
            self.direction.x = 1
            print('RIGHT')
        else:
            self.direction.x = 0
            print('STOP (x)')

    def move(self, dt):
        # normalized movement
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # x axis movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

        # y axis movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

    def update(self, dt):
        self.input()
        self.move(dt)