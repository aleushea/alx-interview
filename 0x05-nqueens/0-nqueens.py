#!/usr/bin/python3
"""N queens solution finder module."""
import sys


solutions = []
"""The list of possible solutions to the N queens problem."""
n = 0
"""The size of the chessboard."""
pos = None
"""The list of possible positions on the chessboard."""


def get_input():
    """Retrieves and validates this program's argument.

    Returns:
        int: The size of the chessboard.
    """
    global n
    n=0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos0, pos1):
    """Checks if the positions of two queens are in an attacking mode.

    Args:
        pos0 (list or tuple): The first queen's position.
        pos1 (list or tuple): The second queen's position.

    Returns:
        bool: True if the queens are in an attacking position, else False.
    """
    return (pos0[0] == pos1[0] or pos0[1] == pos1[1] or
            abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1]))


def group_exists(group):
    """Checks if a group exists in the list of solutions.

    Args:
        group (list of integers): A group of possible positions.

    Returns:
        bool: True if it exists, otherwise False.
    """
    for solution in solutions:
        if all(pos in solution for pos in group):
            return True
    return False


def build_solution(row, group):
    """Builds a solution for the n queens problem.

    Args:
        row (int): The current row in the chessboard.
        group (list of lists of integers): The group of valid positions.
    """
    if row == n:
        if not group_exists(group):
            solutions.append(group.copy())
        return

    for col in range(n):
        pos = (row, col)
        if all(not is_attacking(pos, g_pos) for g_pos in group):
            group.append(pos)
            build_solution(row + 1, group)
            group.pop()


def get_solutions():
    """Gets the solutions for the given chessboard size."""
    global pos, n
    pos = [(x // n, x % n) for x in range(n ** 2)]
    build_solution(0, [])

def backtrack(board, row, n, solutions):
    if row == n:
        solutions.append(board[:])
        return

    for col in range(n):
        board[row] = col
        if is_safe(board, row, col):
            backtrack(board, row + 1, n, solutions)

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(i - row) == abs(board[i] - col):
            return False
    return True

def solveNQueens(n):
    board = [-1] * n
    solutions = []
    backtrack(board, 0, n, solutions)
    return len(solutions)

print(solveNQueens(4))  # Output: 2
print(solveNQueens(5))  # Output: 10
print(solveNQueens(8))  # Output: 92
print(solveNQueens(10)) # Output: 724

n = get_input()
get_solutions()
for solution in solutions:
    print(solution)

