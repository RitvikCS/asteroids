from circleshape import CircleShape
import pygame


class Particle(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, 2)
        self.lifetime = 1.0
        self.color = (255, 255, 255)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

    def update(self, dt):
        self.position += self.velocity * dt
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()
        fade = self.lifetime / 1.0
        self.color = (255, int(255 * fade), int(255 * fade))

    def draw(self, screen):
        pos = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, self.color, pos, self.radius)
