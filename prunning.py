MAX, MIN = 1000, -1000

def alphabeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta):

    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = MIN

        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i,
                            False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = MAX

        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i,
                            True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


# Terminal node values
values = [2, 3, 5, 9, 0, 1, 7, 5]

result = alphabeta(0, 0, True, values, MIN, MAX)

print("Optimal Value:", result)


Algorithm AlphaBeta(node, depth, α, β, maximizingPlayer)

1. If node is a terminal node or depth = 0
      Return node value

2. If maximizingPlayer is TRUE
      value = -∞
      For each child of node
            value = max(value,
                        AlphaBeta(child, depth-1, α, β, FALSE))
            α = max(α, value)
            If α ≥ β
                  Break   // Prune remaining children
      Return value

3. Else (minimizingPlayer)
      value = +∞
      For each child of node
            value = min(value,
                        AlphaBeta(child, depth-1, α, β, TRUE))
            β = min(β, value)
            If α ≥ β
                  Break   // Prune remaining children
      Return value
