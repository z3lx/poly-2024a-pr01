import random
import pygame
from config import *


class Ghost:
    def __init__(
        self,
        pos: tuple[int, int],
        img: pygame.Surface,
        maze: list[list[int]],
        screen: pygame.Surface
    ) -> None:
        self.pos = list(pos)
        self.speed = SPEED
        self.img = img
        self.direction = Direction.UP
        self.dead = False
        self.maze = maze
        self.rect = pygame.Rect(self.pos, GHOST_SIZE)
        self.screen = screen
        self.death_timer = 0
        self.edible = False
        self.edible_img = pygame.transform.scale(
            pygame.image.load('assets/images/powerup.png'),
            GHOST_SIZE
        )
        self.dead_img = pygame.transform.scale(
            pygame.image.load('assets/images/dead.png'),
            GHOST_SIZE
        )

    def draw(self) -> None:
        if not self.dead and not self.edible:
            self.screen.blit(self.img, self.pos)
        elif not self.dead and self.edible:
            self.screen.blit(self.edible_img, self.pos)
        else:
            self.screen.blit(self.dead_img, self.pos)

    def move(self) -> None:
        if not self.dead:
            # Calculate new position and rect
            new_x = self.pos[0] + self.direction[0] * self.speed
            new_y = self.pos[1] + self.direction[1] * self.speed
            new_rect = pygame.Rect(new_x, new_y, GHOST_SIZE[0], GHOST_SIZE[1])

            if not self.check_collision(new_rect):
                # Update position and rect if no collision is detected
                self.pos[0] = new_x
                self.pos[1] = new_y
                self.rect = new_rect
            else:
                # Change direction if a collision is detected
                self.change_direction()

        # Gérer le cas où le fantôme est "mort" avec un timer pour sa résurrection
        elif self.death_timer > 0:
            self.death_timer -= 1

            # Une fois le timer expiré, réinitialiser la position du fantôme et son état
            if self.death_timer == 0:
                # Choisissez une position aléatoire pour réinitialiser le fantôme
                self.pos = random.choice(RANDOM_POS)
                self.dead = False
                self.direction = Direction.UP

    def check_collision(self, rect: pygame.Rect) -> bool:
        # Vérifier si le rectangle du fantôme touche un mur
        for x in range(int(rect.left / TILE_WIDTH), int(rect.right / TILE_WIDTH) + 1):
            for y in range(int(rect.top / TILE_HEIGHT), int(rect.bottom / TILE_HEIGHT) + 1):
                if 0 <= x < len(self.maze[0]) and 0 <= y < len(self.maze):
                    if self.maze[y][x] == 1:  # Vérifier si le fantôme touche un mur
                        return True
        return False

    def die(self) -> None:
        self.dead = True
        self.death_timer = 65

    def change_direction(self) -> None:
        # TODO: Créer une liste de toutes les directions possibles pour le fantôme (gauche, droite, haut, bas)

        # TODO: Mélanger aléatoirement les directions pour simuler un choix aléatoire avec `random.shuffle()`

        # TODO: Parcourir chaque direction et vérifier si elle est valide (pas de collision avec un mur)
            # TODO: Calculer la prochaine position du fantôme en fonction de la direction


            #ßCréer un rectangle représentant cette nouvelle position
            #next_rect = pygame.Rect(next_x, next_y, GHOST_SIZE[0], GHOST_SIZE[1])

            # TODO: Vérifier si cette direction entraîne une collision avec un mur en utilisant `self.check_collision()`
                # TODO: Si aucune collision n'est détectée, définir cette direction comme la nouvelle direction du fantôme avec `self.set_direction()` et sortir de la boucle
                return  # Sortir de la méthode une fois la direction changée

    def stop(self) -> None:
        self.direction = Direction.STOP

    def reset(self) -> None:
        self.pos = random.choice(RANDOM_POS)
        self.dead = False
        self.direction = random.choice([Direction.LEFT, Direction.RIGHT, Direction.UP, Direction.DOWN])
        self.death_timer = 0
        self.edible = False
