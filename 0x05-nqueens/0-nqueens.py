#!/usr/bin/python3
"""N queens solution finder module."""
import sys

def backtrack(board, row, n, solutions):
    if row == n:
        solutions.append([f"[{i}]" for i in board])
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
    return solutions

if __name__ == "__main__":
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

    solutions = solveNQueens(n)
    for solution in solutions:
        print(solution)
