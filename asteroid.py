import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    
    def draw(self, screen):
        pygame.draw.circle(screen, (200,200,200),(int(self.position.x),int(self.position.y)), int(self.radius),2)

    def update(self, dt):
        self.position+=self.velocity*dt
        
    def split(self):
        
        old_radius=self.radius
        old_velocity=self.velocity
        old_position = self.position.copy()
        self.kill()
        if old_radius<=ASTEROID_MIN_RADIUS:
            return
        

        random_angle = random.uniform(20,50)

        vel1=old_velocity.rotate(random_angle)*1.2
        vel2=old_velocity.rotate(-random_angle)*1.2

        new_radius=old_radius - ASTEROID_MIN_RADIUS
        a1=Asteroid(old_position.x, old_position.y, new_radius)
        a2=Asteroid(old_position.x, old_position.y, new_radius)

        a1.velocity=vel1
        a2.velocity=vel2



    

