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


def create_coins(board: List[List[int]]) -> List[tuple]:
    coins = []

    for y in range(1, len(board) - 1):
        for x in range(1, len(board[y]) - 1):
            if board[y][x] == 0:
                coins.append((x, y))

    for pos in special_coins_pos:
        coins.remove(pos)

    return coins


def create_special_coins(board):
    special_coins = []

    for pos in special_coins_pos:
        special_coins.append(pos)

    return special_coins
