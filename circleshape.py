import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self,x,y,radius):
        if hasattr(self,"containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0) 
        self.radius = radius
    
    def draw(self,screen):
        #override in subclass
        pass
    def update(self,dt):
        #override in subclass
        pass
    def collisionCheck(self,shape):
        return self.position.distance_to(shape.position) < (self.radius + shape.radius)