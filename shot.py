import pygame
from circleshape import *
from constants import *



class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = velocity

    def update(self, dt):
        self.position += self.velocity*dt
        

    def draw(self, screen):
        pygame.draw.circle(
            screen, (255, 255, 255),
            (int(self.position.x), int(self.position.y)),
            int(self.radius), 0
        )