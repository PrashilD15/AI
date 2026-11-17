# Practical 6: 8 Queens Problem using Backtracking
N = 8


def is_safe(board, row, col):
    """Check if a queen can be safely placed at board[row][col]."""
    # Check previous rows
    for i in range(row):
        # Same column
        if board[i] == col:
            return False
        # Diagonal check
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve(board, row):
    """Recursively place queens using backtracking."""
    # All queens are placed
    if row == N:
        return True

    for col in range(N):
        if is_safe(board, row, col):
            # Place queen
            board[row] = col
            if solve(board, row + 1):
                return True
            # Backtrack
            board[row] = -1

    return False


if __name__ == "__main__":
    # Initially, no queens are placed (-1 indicates empty)
    board = [-1] * N

    if solve(board, 0):
        print("Solution:")
        for row in range(N):
            for col in range(N):
                if board[row] == col:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
    else:
        print("No solution exists.")
