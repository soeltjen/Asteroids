import pygame
import player
from constants import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    p1 = player.Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    updatable = pygame.sprite.Group(p1)
    drawable = pygame.sprite.Group(p1)
    p1.containers = (updatable,drawable)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        dt = clock.tick(60)/1000
        updatable.update(dt)
        # drawable.draw(screen)
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()


    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()