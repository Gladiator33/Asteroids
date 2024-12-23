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

score = 0
game_over = False
global score_font

def load_high_score():
    try:
        with open("high_score.txt", "r") as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 0

high_score = load_high_score()

def save_high_score(score):
    global high_score
    if score > load_high_score():
        high_score = score
        with open("high_score.txt", "w") as file:
            file.write(str(score))

def handle_events():
    global game_over
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            import sys
            sys.exit()
        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_over = False
                save_high_score(score)
                return reset_game()
    return None

def update_game_logic(dt, player):
    for thing in updatable:
        thing.update(dt)
    check_collisions(player)

def draw_objects(screen):
    for thing in drawable:
        thing.draw(screen)
    score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
    score_rect = score_text.get_rect(topright=(SCREEN_WIDTH - 10, 10))
    screen.blit(score_text, score_rect)

def check_collisions(player):
    global game_over
    for asteroid in asteroids:
        if player.collisions(asteroid):
            player.kill()
            game_over = True
            
    for asteroid in asteroids:
        global score
        for shot in shots:
            if shot.collisions(asteroid):
                asteroid.split()
                shot.kill()
                score += 100
    return False

def reset_game():
    global score
    asteroids.empty()
    shots.empty()
    updatable.empty()
    drawable.empty()
    thruster_group.empty()
    score = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player (x, y)

    asteroid_field = AsteroidField()

    return player

 
 
def main():
    global score_font
    pygame.init()
    score_font = pygame.font.Font(None, 36)
    font = pygame.font.Font(None, 74)
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
        new_player = handle_events()
        if new_player:
            player = new_player
        update_game_logic(dt, player)    
        draw_objects(screen)

        for thruster in list(thruster_group):
            thruster_group.update(dt)
            if thruster.lifetime <= 0:
                thruster_group.remove(thruster)
        
        for thruster in thruster_group:
            pygame.draw.circle(screen, thruster.color, thruster.position, thruster.radius)



        if game_over:
            global score
            text = font.render("GAME OVER!", True, (255, 0, 0))
            text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            screen.blit(text, text_rect)
            
            # Smaller font for instruction text
            small_font = pygame.font.Font(None, 36)  # Size 36 instead of 74
            restart_text = small_font.render("Press R to restart", True, (255, 255, 255))
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 150))
            end_score_text = small_font.render(f"Final score: {score}", True, (255, 255, 255))
            end_score_rect = end_score_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50))
            if score >= high_score:
                highscore_text = small_font.render("New Highscore!", True, (255, 255, 255))
            else:
                highscore_text = small_font.render(f"Highscore: {high_score}", True, (255, 255, 255))
            highscore_rect = highscore_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 100))
            screen.blit(highscore_text, highscore_rect)
            screen.blit(restart_text, restart_rect, )
            screen.blit(end_score_text, end_score_rect)

        pygame.display.flip()
    
        dt = clock.tick(60) / 1000


    

if __name__ == "__main__":
    main()