from constants import *
from circleshape import *
class Thruster(CircleShape):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, THRUSTER_RADIUS)  # You'll need to define THRUSTER_RADIUS
        self.lifetime = 0.5  # Adjust as needed for desired effect
        self.color = color

    def update(self, dt):
        super().update(dt)
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()