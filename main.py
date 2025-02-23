# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player  # Import the Player class

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("My Asteroids project")

    clock = pygame.time.Clock()
    dt = 0

    # Create player object at the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update player (handles rotation)
        player.update(dt)

        screen.fill((0, 0, 0))  # Clear screen
        
        player.draw(screen)  # Draw the player

        pygame.display.flip()  # Update the display

        dt = clock.tick(60) / 1000  # Maintain 60 FPS

if __name__ == "__main__":
    main()
