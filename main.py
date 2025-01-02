import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import *
import sys

from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for i in updatable:
            i.update(dt)

        for asteroid in asteroids:
            if asteroid.collisions(player):
                pygame.quit()
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collisions(shot):
                    shot.kill()
                    asteroid.kill()

        screen.fill("black")

        for i in drawable:
            i.draw(screen)

        pygame.display.flip()
        dt = timer.tick(60) / 1000


if __name__ == "__main__":
    main()
