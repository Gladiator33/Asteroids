from constants import *
from circleshape import *
class Thruster(CircleShape):
    def __init__(self, x, y, radius, color, lifetime):
        super().__init__(x, y, radius) 
        self.color = color
        self.lifetime = lifetime

    def update(self, dt):
        super().update(dt)
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()