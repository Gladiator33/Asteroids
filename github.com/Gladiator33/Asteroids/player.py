from circleshape import *
from constants import *
from shot import *
from thruster import *
from game_objects import thruster_group

class Player(CircleShape):
    def __init__(self, x,y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw (self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    def rotate(self, dt):
        self.rotation -= PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys [pygame.K_w]:
            self.move(dt)
        if keys [pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y, PLAYER_SHOT_RADIUS)
        new_shot.fire(self.rotation)
    
    def create_thruster_effect(self):
        thruster = Thruster(self.position.x, self.position.y)
        direction = pygame.Vector2(0, 1).rotate(-self.rotation)
        thruster.velocity = direction * THRUSTER_SPEED  # Define THRUSTER_SPEED
        thruster_group.add(thruster)