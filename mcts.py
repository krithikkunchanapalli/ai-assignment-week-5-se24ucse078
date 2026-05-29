# Monte Carlo Tree Search (Simple Version)

import random


class State:

    def __init__(self):
        pass

    def simulate(self):
        return random.choice([0, 1])


class Node:

    def __init__(self):
        self.visits = 0
        self.wins = 0


def monte_carlo_tree_search(iterations):

    node = Node()

    for i in range(iterations):

        state = State()

        result = state.simulate()

        node.visits += 1
        node.wins += result

    return node.wins / node.visits


iterations = 1000

win_rate = monte_carlo_tree_search(iterations)

print("Iterations:", iterations)
print("Estimated Win Rate:", win_rate)