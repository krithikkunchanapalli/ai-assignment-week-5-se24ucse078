# Heuristic Alpha Beta Search

class Node:

    def __init__(self, value=None):
        self.value = value
        self.children = []


def heuristic(node):
    return node.value


def alpha_beta(node, depth, alpha, beta, maximizing):

    if depth == 0 or len(node.children) == 0:
        return heuristic(node)

    if maximizing:

        best = -1000

        for child in node.children:

            value = alpha_beta(
                child,
                depth - 1,
                alpha,
                beta,
                False
            )

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:

        best = 1000

        for child in node.children:

            value = alpha_beta(
                child,
                depth - 1,
                alpha,
                beta,
                True
            )

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


root = Node()

left = Node()
right = Node()

root.children = [left, right]

left.children = [Node(5), Node(8)]
right.children = [Node(2), Node(7)]

result = alpha_beta(
    root,
    2,
    -1000,
    1000,
    True
)

print("Best Heuristic Value:", result)