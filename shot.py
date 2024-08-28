from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,SHOT_RADIUS)
    def draw(self,screen):
        pygame.draw.circle(screen,"yellow",self.position,SHOT_RADIUS,1)
    def update(self,dt):
        self.position += (self.velocity * dt)