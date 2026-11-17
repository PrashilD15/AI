# Practical 8: Tic-Tac-Toe Game with AI using Minimax Algorithm


def print_board(board):
    """Display the 3x3 game board."""
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")


def check_winner(board):
    """Check if either player has won or if the game is a draw."""
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c]:
            if board[a] == "X":
                return 1
            if board[a] == "O":
                return -1
    if all(cell in ("X", "O") for cell in board):
        return 0
    return None


def minimax(board, is_max):
    """Minimax recursive evaluation function."""
    result = check_winner(board)
    if result is not None:
        return result

    if is_max:
        best = -float("inf")
        for i in range(9):
            if board[i] not in ("X", "O"):
                board[i] = "X"
                score = minimax(board, False)
                board[i] = str(i + 1)
                best = max(best, score)
        return best
    else:
        best = float("inf")
        for i in range(9):
            if board[i] not in ("X", "O"):
                board[i] = "O"
                score = minimax(board, True)
                board[i] = str(i + 1)
                best = min(best, score)
        return best


def best_move(board):
    """Find the optimal move for AI (X) using Minimax."""
    best_score = -float("inf")
    move = -1
    for i in range(9):
        if board[i] not in ("X", "O"):
            board[i] = "X"
            score = minimax(board, False)
            board[i] = str(i + 1)
            if score > best_score:
                best_score = score
                move = i
    return move


if __name__ == "__main__":
    board = [str(i) for i in range(1, 10)]
    print("Tic-Tac-Toe: You are O, AI is X")

    while True:
        print_board(board)

        # AI move
        move = best_move(board)
        board[move] = "X"
        print("\nAI played:")
        print_board(board)

        result = check_winner(board)
        if result is not None:
            break

        # Human move
        pos = int(input("Enter position (1-9): ")) - 1
        if pos < 0 or pos > 8 or board[pos] in ("X", "O"):
            print("Invalid move! Try again.")
            board[move] = str(move + 1)
            continue

        board[pos] = "O"
        result = check_winner(board)
        if result is not None:
            break

    print("\nFinal Board:")
    print_board(board)

    if result == 1:
        print("AI wins!")
    elif result == -1:
        print("You win!")
    else:
        print("Match Draw!")
