from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
    
        def draw():
            pygame.draw.circle(self.x, self.y, self.radius, 2)
        
        def update(dt):
            self.position += self.velocity * dt