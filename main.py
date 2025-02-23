import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("My Asteroids project")

    clock = pygame.time.Clock()
    dt = 0

    # Create groups
    updatable = pygame.sprite.Group()  # All objects that can be updated
    drawable = pygame.sprite.Group()   # All objects that can be drawn
    asteroids = pygame.sprite.Group()  # All asteroids
    shots = pygame.sprite.Group()      # All shots

    # Set static containers for Asteroid, Shot, and AsteroidField
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)

    # Create player object at the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Add the player to updatable and drawable groups
    updatable.add(player)
    drawable.add(player)

    # Create AsteroidField object
    asteroid_field = AsteroidField()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update all updatable objects
        updatable.update(dt)

        # Check for collisions between the player and asteroids
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                return  # Exit the game immediately

        # Check for collisions between bullets and asteroids
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()  # Split the asteroid
                    shot.kill()      # Remove the bullet
                    break  # Exit the inner loop since the bullet is already destroyed

        screen.fill((0, 0, 0))  # Clear screen

        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()  # Update the display

        dt = clock.tick(60) / 1000  # Maintain 60 FPS

if __name__ == "__main__":
    main()