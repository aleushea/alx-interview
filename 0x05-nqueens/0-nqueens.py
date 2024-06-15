#!/usr/bin/python3
"""N queens solution finder module."""
import sys

SOLUTIONS = []
"""The list of possible solutions to the N queens problem."""
N = 0
"""The size of the chessboard."""
POSSIBLE_POSITIONS = None
"""The list of possible positions on the chessboard."""


def get_input():
    """Retrieve and validate the program's argument.

    Returns:
        int: The size of the chessboard.
    """
    global N
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    return N


def is_attacking(position_a, position_b):
    """Check if the positions of two queens are in an attacking mode.

    Args:
        position_a (list or tuple): The first queen's position.
        position_b (list or tuple): The second queen's position.

    Returns:
        bool: True if the queens are in an attacking position, else False.
    """
    return (position_a[0] == position_b[0] or
            position_a[1] == position_b[1] or
            abs(position_a[0] - position_b[0]) == abs(position_a[1] - position_b[1]))


def group_exists(group):
    """Check if a group exists in the list of solutions.

    Args:
        group (list of integers): A group of possible positions.

    Returns:
        bool: True if it exists, otherwise False.
    """
    for solution in SOLUTIONS:
        if all(position in solution for position in group):
            return True
    return False


def build_solution(row, group):
    """Build a solution for the n queens problem.

    Args:
        row (int): The current row in the chessboard.
        group (list of lists of integers): The group of valid positions.
    """
    if row == N:
        if not group_exists(group):
            SOLUTIONS.append(group.copy())
        return

    for col in range(N):
        position = (row, col)
        if all(not is_attacking(position, g_position) for g_position in group):
            group.append(position)
            build_solution(row + 1, group)
            group.pop()


def get_solutions():
    """Get the solutions for the given chessboard size."""
    global POSSIBLE_POSITIONS, N
    POSSIBLE_POSITIONS = [(x // N, x % N) for x in range(N ** 2)]
    build_solution(0, [])


N = get_input()
get_solutions()
for solution in SOLUTIONS:
    print(solution)

