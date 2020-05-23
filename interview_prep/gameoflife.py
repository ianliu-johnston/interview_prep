from copy import deepcopy
import logging
from typing import Any, List

log = logging.getLogger(__name__)
alive = 1
dead = 0


def cell_survival(cell: bool, population: int) -> bool:
    """
    control flow for cell survival
    :param cell: cell to check
    :param population: how many cells are alive
    :return: If cell will live(True) or die(False) based on rules
    """
    if cell is alive and (population == 2 or population == 3):
        return alive
    if cell is dead and population == 3:
        return alive
    return dead


def get_population(board: List[List[bool]], x: int, y: int) -> List[Any]:
    """
    calculate the population. there are 8 possible neighbors in a 2D array

    :param board: 2D matrix of cells
    :param x: x location in 2D matrix
    :param y: y location in 2D matrix
    :return: total number of live neighbors
    """
    population = 0
    num_rows = len(board)
    num_cols = len(board[0])
    for row_index in range(3):
        scope_x_index = x + (row_index - 1)
        if scope_x_index < 0 or scope_x_index >= num_rows:
            continue
        for col_index in range(3):
            scope_y_index = y + (col_index - 1)
            if (scope_y_index < 0 or scope_y_index > num_cols-1) or\
               (col_index == 1 and row_index == 1):  # skip the cell itself
                continue
            if board[scope_x_index][scope_y_index] == 1:
                population += 1
    log.debug("{},{}:Population:{}".format(x, y, population))
    return population


def game_of_life(board: List[List[bool]]) -> List[List[bool]]:
    """
    main loop implements checking neighbors
    :param board: 2D matrix of cells
    :return: next evolution of the matrix of cells
    """
    evolve = deepcopy(board)
    for row_index, row in enumerate(board):
        log.debug(f"Row {row_index}")
        for col_index, cell in enumerate(row):
            population = get_population(board, row_index, col_index)
            state = cell_survival(cell, population)
            log.debug("population:{}; {}=={}?{}".format(
                      population, state, cell, state == cell))
            if cell != state:
                evolve[row_index][col_index] = state
    log.debug(evolve)
    return evolve
