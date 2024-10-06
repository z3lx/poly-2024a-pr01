from typing import List

special_coins_pos = [(1, 1), (14, 1), (1, 13), (14, 13)]


def create_board() -> List[List[int]]:

    # TODO Create a board with the following structure
    # 1 -> Wall
    # 0 -> Path

    maze = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Top boundary
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # Path
        [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],  # Internal walls
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],  # Paths
        [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1],  # Complex paths
        [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # Open path area
        [1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],  # Narrow passage
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],  # Large open path
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],  # Solid wall section
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # Path
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],  # Complex wall structure
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],  # More paths
        [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],  # Internal walls
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # Open path
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Extra boundary row
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Extra boundary row
    ]

    return maze

def create_coins(board):
    coins = []

    coins.append((1, 1)) # Placeholder, ligne à retirer

    # TODO: Ajouter la position de toutes les cases '0' à la variable coins. Pour ajouter un élément, vous pouvez utiliser l'expression suivante :
    # coins.append((x, y))
    # en remplacant x et y par la position. Notez que le premier coin est à la position (1, 1)

    # TODO: Retirer les coins de chaque "coin" du carré. Vous devez utiliser la variable 'special_coins_pos' et la fonction 'remove'.

    return coins

def create_special_coins(board):
    special_coins = []

    # TODO: Ajouter des coins aux positions spéciales, en utilisant la variable 'special_coins_pos'.
    
    return special_coins
