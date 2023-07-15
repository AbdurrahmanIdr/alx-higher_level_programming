#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    # Check if the current position is safe for the queen
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    # Create an empty chessboard
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def backtrack(col):
        if col >= N:
            # Found a solution, add it to the solutions list
            solution = [[row, col] for row in range(N) if board[row][col] == 1]
            solutions.append(solution)
            return

        for row in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                backtrack(col + 1)
                board[row][col] = 0

    backtrack(0)

    return solutions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
        """_summary_
        """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)

    for solution in solutions:
        print(solution)
