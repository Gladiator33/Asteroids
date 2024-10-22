import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from game_objects import updatable, drawable, thruster_group

asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
Shot.containers = (shots, updatable, drawable)
Thruster.containers = (thruster_group, updatable, drawable)

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            import sys
            sys.exit()

def update_game_logic(dt, player):
    for thing in updatable:
        thing.update(dt)
    check_collisions(player)

def draw_objects(screen):
    for thing in drawable:
        thing.draw(screen)

def check_collisions(player):
    for asteroid in asteroids:
        if player.collisions(asteroid):
            print("Game Over!")
            import sys
            sys.exit()
            
    for asteroid in asteroids:
        for shot in shots:
            if shot.collisions(asteroid):
                asteroid.split()
                asteroid.kill()
                shot.kill()

 
 
def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    asteroid_field = AsteroidField()

    while True:
        screen.fill((0 ,0 ,0))
        handle_events()
        update_game_logic(dt, player)    
        draw_objects(screen)

        for thruster in list(thruster_group):
            thruster_group.update(dt)
            if thruster.lifetime <= 0:
                thruster_group.remove(thruster)
        
        for thruster in thruster_group:
            pygame.draw.circle(screen, thruster.color, thruster.position, thruster.radius)
        
        pygame.display.flip()
    
        dt = clock.tick(60) / 1000


    

if __name__ == "__main__":
    main()