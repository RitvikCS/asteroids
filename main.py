import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from particle import Particle
from player import *
import sys

from shot import Shot


def draw_score(screen, score):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (640, 10))


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    particles = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    Particle.containers = (updatable, drawable, particles)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0

    score = 0

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
                print(f"Final Score: {score}")
                sys.exit()
            for shot in shots:
                if asteroid.collisions(shot):
                    # print("Collision Detected")
                    shot.kill()
                    # print("Shot Killed")
                    split_result = asteroid.split()
                    # print(f"Split Result {split_result}")
                    if split_result == 2:
                        score += 2
                    else:
                        score += 1

        screen.fill("black")

        for i in drawable:
            i.draw(screen)

        draw_score(screen, score)
        pygame.display.flip()
        dt = timer.tick(60) / 1000


if __name__ == "__main__":
    main()
