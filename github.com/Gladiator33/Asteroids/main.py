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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0 ,0 ,0))

        for thing in updatable:
            thing.update(dt)

        for asteroid in asteroids:
            if player.collisions(asteroid):
                print("Game Over!")
                import sys
                sys.exit()

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
    
        dt = clock.tick(60) / 1000


    

if __name__ == "__main__":
    main()