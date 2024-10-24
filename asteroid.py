from circleshape import *
from constants import *
import pygame
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  
        self.velocity = pygame.Vector2(0, 0) 
    
    def draw(self,screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), int(self.radius), 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vector1 = self.velocity.rotate(random_angle) * 1.2
            vector2 = self.velocity.rotate(-random_angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = vector1
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = vector2