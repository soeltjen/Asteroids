import pygame
from player import Player
from constants import *
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
import sys

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots,updatable,drawable)


    p1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    astfield = AsteroidField()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for a in asteroids:
            if a.collisionCheck(p1):
                print("Game over!")
                sys.exit()
            for s in shots:
                if s.collisionCheck(a):
                    s.kill()
                    a.split()

        screen.fill((0,0,0))

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000

    print("Starting asteroids!")
if __name__ == "__main__":
    main()