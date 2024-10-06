from typing import Tuple

import pygame
import sys
from config import EDIBLE_GHOST_TIMER, RESET_POS1, RESET_POS3, RESET_POS4
from ghost import *
from pacman import PacMan
from helper import create_board, create_special_coins
from helper import create_coins
from end import End
import threading


class Game:
    def __init__(self, screen):
        # Initialiser les paramètres du jeu
        self.screen = screen
        self.board = create_board()
        self.coins = create_coins(self.board)
        self.special_coins = create_special_coins(self.board)

        self.pacman = PacMan(self.screen, self.board)
        pygame.display.set_caption("Pac-Man")
        self.font = pygame.font.Font(None, 36)
        self.score = 0
        self.wall_color = (0, 0, 255)

        # Charger les images des fantômes
        red_ghost = pygame.transform.scale(
            pygame.image.load('assets/images/red.png'),
            GHOST_SIZE
        )
        blue_ghost = pygame.transform.scale(
            pygame.image.load('assets/images/blue.png'),
            GHOST_SIZE
        )
        orange_ghost = pygame.transform.scale(
            pygame.image.load('assets/images/orange.png'),
            GHOST_SIZE
        )
        pink_ghost = pygame.transform.scale(
            pygame.image.load('assets/images/pink.png'),
            GHOST_SIZE
        )

        # Créer les fantômes
        self.red_ghost_instance = Ghost(
            pos=RESET_POS1,
            img=red_ghost,
            maze=self.board,
            screen=screen
        )
        self.blue_ghost_instance = Ghost(
            pos=RESET_POS2,
            img=blue_ghost,
            maze=self.board,
            screen=screen
        )
        self.orange_ghost_instance = Ghost(
            pos=RESET_POS3,
            img=orange_ghost,
            maze=self.board,
            screen=screen
        )
        self.pink_ghost_instance = Ghost(
            pos=RESET_POS4,
            img=pink_ghost,
            maze=self.board,
            screen=screen
        )

        self.ghosts = [
            self.red_ghost_instance,
            self.blue_ghost_instance,
            self.orange_ghost_instance,
            self.pink_ghost_instance
        ]

        self.end = End()
        self.game_over = False
        self.game_won = False

    def start(self):
        # Initialiser les paramètres du jeu
        self.board = create_board()

    def render(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 1:
                    pygame.draw.rect(
                        self.screen,
                        (0, 0, 0),
                        (col * 50, row * 50, 50, 50)
                    )

                    # Draw the borders
                    thickness = 7

                    # Top border
                    if row > 0 and self.board[row - 1][col] == 0:
                        pygame.draw.line(
                            self.screen,
                            self.wall_color,
                            (col * 50, row * 50),
                            (col * 50 + 50, row * 50),
                            thickness
                        )

                    # Bottom border
                    if row < len(self.board) - 1 and self.board[row + 1][col] == 0:
                        pygame.draw.line(
                            self.screen,
                            self.wall_color,
                            (col * 50, row * 50 + 50),
                            (col * 50 + 50, row * 50 + 50),
                            thickness
                        )

                    # Left border
                    if col > 0 and self.board[row][col - 1] == 0:
                        pygame.draw.line(
                            self.screen,
                            self.wall_color,
                            (col * 50, row * 50),
                            (col * 50, row * 50 + 50),
                            thickness
                        )

                    # Right border
                    if col < len(self.board[row]) - 1 and self.board[row][col + 1] == 0:
                        pygame.draw.line(
                            self.screen,
                            self.wall_color,
                            (col * 50 + 50, row * 50),
                            (col * 50 + 50, row * 50 + 50),
                            thickness
                        )
                else:
                    # Draw the empty cells
                    pygame.draw.rect(
                        self.screen,
                        (255, 255, 255),
                        (col * 50, row * 50, 50, 50)
                    )

                    # Draw the coins
                    if (col, row) in self.coins:
                        pygame.draw.circle(
                            self.screen,
                            (255, 215, 0),
                            (col * 50 + 25, row * 50 + 25),
                            4
                        )

                    # Draw the special coins
                    if (col, row) in self.special_coins:
                        pygame.draw.circle(
                            self.screen,
                            (255, 215, 0),
                            (col * 50 + 25, row * 50 + 25),
                            8
                        )

        # Draw the score
        score_text = self.font.render(
            "Score: " + str(self.score),
            True,
            (255, 255, 255)
        )
        self.screen.blit(score_text, (50, 50 * 14))

        # Draw the number of lives
        lives_text = self.font.render(
            "Lives: ",
            True,
            (255, 255, 255)
        )
        self.screen.blit(lives_text, (50, 50 * 15))

        pacman_image = pygame.transform.scale(
            pygame.image.load('assets/images/pacman.png'),
            (30, 30)
        )
        for i in range(self.pacman.lives):
            self.screen.blit(pacman_image, (150 + i * 40, 50 * 15))

    def handle_keypress(self, event: pygame.event.Event) -> None:
        if event.key == pygame.K_RIGHT:
            if self.check_collision((1, 0)):
                self.pacman.set_direction((1, 0))
        elif event.key == pygame.K_LEFT:
            if self.check_collision((-1, 0)):
                self.pacman.set_direction((-1, 0))
        elif event.key == pygame.K_UP:
            if self.check_collision((0, -1)):
                self.pacman.set_direction((0, -1))
        elif event.key == pygame.K_DOWN:
            if self.check_collision((0, 1)):
                self.pacman.set_direction((0, 1))

    def check_collision(self, direction: Tuple[int, int]) -> bool:
        dx, dy = direction
        new_x = self.pacman.x + dx
        new_y = self.pacman.y + dy
        if self.board[new_y][new_x] == 0:
            return True
        return False

    def update(self):
        for ghost in self.ghosts:
            ghost.draw()
            ghost.move()
        self.check_collision_between_ghosts_and_pacman()
        self.pacman.move()
        self.pacman.draw()
        self.check_score()
        self.check_special_coins()

    def check_score(self):
        # TODO: Vérifier si la position actuelle de Pac-Man (en coordonnées de grille) correspond à une position de pièce en utilisant (self.pacman.x, self.pacman.y)
            # TODO: Si Pac-Man est sur une pièce, la retirer de la liste des pièces restantes à collecter

            # TODO: Ajouter des points au score du joueur pour la pièce collectée (par exemple, 10 points)

        if len(self.coins) == 0:
            self.end.render(True)
            self.game_won = True
            self.game_over = True

    def check_special_coins(self):
        pass
        # TODO: Vérifier si la position actuelle de Pac-Man (en coordonnées de grille) correspond à une position de pièce spéciale

            # TODO: Si Pac-Man est sur une pièce spéciale, retirer cette pièce spéciale de la liste

            # TODO: Ajouter des points au score du joueur pour la pièce spéciale collectée

            # TODO: Activer le mode "manger" en appelant la méthode appropriée pour activer le mode "manger" des fantômes avec self.activate_eat_mode()

    def activate_eat_mode(self):
        timer = threading.Timer(EDIBLE_GHOST_TIMER, self.deactivate_eat_mode)
        timer.start()

        # Make the ghosts edible
        self.red_ghost_instance.edible = True
        self.blue_ghost_instance.edible = True
        self.orange_ghost_instance.edible = True
        self.pink_ghost_instance.edible = True

        self.red_ghost_instance.draw()
        self.blue_ghost_instance.draw()
        self.orange_ghost_instance.draw()
        self.pink_ghost_instance.draw()

    def deactivate_eat_mode(self):
        # Code to deactivate eat mode
        self.red_ghost_instance.edible = False
        self.blue_ghost_instance.edible = False
        self.orange_ghost_instance.edible = False
        self.pink_ghost_instance.edible = False

        self.red_ghost_instance.draw()
        self.blue_ghost_instance.draw()
        self.orange_ghost_instance.draw()
        self.pink_ghost_instance.draw()

    def check_collision_between_ghosts_and_pacman(self):
        for ghost in self.ghosts:
            if ghost.rect.colliderect(self.pacman.rect):
                if ghost.edible:
                    ghost.stop()
                    ghost.die()
                elif not ghost.dead:
                    # Game over
                    if self.pacman.die():
                        self.red_ghost_instance.stop()
                        self.blue_ghost_instance.stop()
                        self.orange_ghost_instance.stop()
                        self.pink_ghost_instance.stop()
                        self.game_over = True
                        self.end.render(False)
                        return
                    self.pacman.reset()
                    self.red_ghost_instance.reset()
                    self.blue_ghost_instance.reset()
                    self.orange_ghost_instance.reset()
                    self.pink_ghost_instance.reset()
