from circleshape import *
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  
        self.velocity = pygame.Vector2(0, 0) 
        self.groups()
    
    def draw(self,screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), int(self.radius), 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
    def fire(self, direction):
        self.velocity = pygame.Vector2(0, 1).rotate(direction) * PLAYER_SHOT_SPEED