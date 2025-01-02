import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        # print(f"Current radius: {self.radius}")  # Debug print
        # print(f"Min radius: {ASTEROID_MIN_RADIUS}")
        if self.radius <= ASTEROID_MIN_RADIUS:
            # print("Destroying small asteroid")
            return 2
        else:
            # print("Splitting large asteroid")
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            if new_radius > 0:
                random_angle = random.uniform(20, 50)
                direction_1 = self.velocity.rotate(random_angle)
                direction_2 = self.velocity.rotate(-random_angle)
                obj1 = Asteroid(self.position.x, self.position.y, new_radius)
                obj1.velocity = direction_1 * 1.2
                obj2 = Asteroid(self.position.x, self.position.y, new_radius)
                obj2.velocity = direction_2 * 1.2
            return 1
