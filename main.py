import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for u in updatable:
            u.update(dt)
        
        for a in asteroids:
            if player.check_for_collisions(a):
                print(f"Game over! Final score: {score}")
                raise SystemExit()
            for s in shots:
                if a.check_for_collisions(s):
                    score += ASTEROID_MAX_RADIUS - a.radius + ASTEROID_MIN_RADIUS
                    a.split()
                    s.kill()
            
        pygame.Surface.fill(screen, "black")
        
        for d in drawable:
            d.draw(screen)
        
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = font.render(f"Score: {int(score)}", False, "orange")
        screen.blit(text_surface, (10, 10))
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()