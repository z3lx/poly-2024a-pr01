from typing import List, Tuple
import pygame
from config import *


class PacMan:
    def __init__(self, screen: pygame.Surface, board: List[List[int]]) -> None:
        self.screen = screen
        self.board = board
        self.x, self.y = PACMAN_START_POS
        self.size = 40
        self.color = (255, 255, 0)
        self.size_grid = 50
        self.direction = None
        self.frame_count = 0
        self.changed_direction = None
        self.mouth_open_angle = 45
        self.lives = 3
        self.screen_pos = grid_to_screen(
            grid_pos=[self.x, self.y],
            tile_size=[self.size_grid, self.size_grid]
        )
        self.rect = pygame.Rect(self.screen_pos, PACMAN_SIZE)

    def draw(self) -> None:
        # Load the Pac-Man image
        pacman_image = pygame.image.load('assets/images/pacman.png')
        pacman_image = pygame.transform.scale(pacman_image, (self.size, self.size))

        # Rotate the image based on the direction
        if self.direction is None or self.direction == (1, 0):  # Right
            rotated_image = pacman_image
        elif self.direction == (-1, 0):  # Left
            rotated_image = pygame.transform.rotate(pacman_image, 180)
        elif self.direction == (0, -1):  # Down
            rotated_image = pygame.transform.rotate(pacman_image, 90)
        elif self.direction == (0, 1):  # Up
            rotated_image = pygame.transform.rotate(pacman_image, 270)

        # Calculate the screen position of Pac-Man
        screen_x = self.x * self.size_grid
        screen_y = self.y * self.size_grid

        # Draw the rotated image at the current position
        self.screen.blit(rotated_image, (screen_x, screen_y))

    def move(self) -> None:
        if not self.direction:
            return

        # Calculate new position
        dx, dy = self.direction
        new_x = self.x + dx
        new_y = self.y + dy

        # Check for collisions with walls
        if self.board[new_y][new_x] == 1:
            return

        # Update position
        self.x, self.y = new_x, new_y

        # Update rect
        self.screen_pos = grid_to_screen(
            grid_pos=[self.x, self.y],
            tile_size=[self.size_grid, self.size_grid]
        )
        self.rect.topleft = self.screen_pos

    def set_direction(self, direction: Tuple[int, int]) -> None:
        self.direction = direction

    def stop(self) -> None:
        self.direction = None

    def reset(self) -> None:
        self.x, self.y = PACMAN_START_POS
        self.direction = None

    def die(self) -> bool:
        if self.lives == 0:
            return True
        self.lives -= 1
        self.reset()
        return False
