#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True

def print_solution(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    
def solve_nqueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    def backtrack(row):
        if row == n:
            print_solution(board)
            print()
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0

    backtrack(0)

if __name__ == "__main__":
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

    solve_nqueens(N)
