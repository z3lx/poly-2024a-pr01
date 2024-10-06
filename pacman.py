import math
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

        # TODO: Extraire la direction de déplacement à partir de l'attribut `self.direction`.

        # TODO: Calculer les nouvelles coordonnées X et Y en fonction de la direction
        # Ajouter la direction à la position actuelle (self.x, self.y) pour obtenir la nouvelle position.

        # TODO: Vérifier si la nouvelle position entre en collision avec un mur
        # Utiliser `self.board[new_y][new_x]` pour voir si la case correspond à un chemin (0) ou à un mur (1).

            # TODO: Mettre à jour la position de Pac-Man si aucun mur n'est rencontré

            # TODO: Convertir les nouvelles coordonnées de la grille en position à l'écran
            # Utiliser une fonction comme `grid_to_screen` pour obtenir les coordonnées sur l'écran.

            # TODO: Mettre à jour la position du rectangle de Pac-Man dans l'interface
            # Mettre à jour `self.rect.topleft` avec la nouvelle position à l'écran pour déplacer l'affichage de Pac-Man.

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
