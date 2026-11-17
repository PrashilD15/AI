# Practical 4: Minimax with Alpha-Beta Pruning


def minimax(depth, index, is_max, values, alpha, beta):
    """
    Minimax search with Alpha-Beta Pruning.
    depth: current tree level
    index: index of the current node in the values array at depth 3
    is_max: boolean indicating if current player is Maximizer
    values: list of leaf node evaluation values
    alpha: best value that maximizer can guarantee
    beta: best value that minimizer can guarantee
    """
    # Base condition: leaf node
    if depth == 3:
        return values[index]

    if is_max:
        best = float('-inf')
        for i in range(2):
            value = minimax(
                depth + 1,
                index * 2 + i,
                False,
                values,
                alpha,
                beta
            )
            best = max(best, value)
            alpha = max(alpha, best)
            # Pruning condition
            if alpha >= beta:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            value = minimax(
                depth + 1,
                index * 2 + i,
                True,
                values,
                alpha,
                beta
            )
            best = min(best, value)
            beta = min(beta, best)
            # Pruning condition
            if alpha >= beta:
                break
        return best


if __name__ == "__main__":
    # Leaf node values
    values = [3, 5, 6, 9, 1, 2, 0, -1]

    # Initial values for alpha and beta
    alpha = float('-inf')
    beta = float('inf')

    # Find optimal value
    result = minimax(0, 0, True, values, alpha, beta)
    print("Optimal value:", result)
