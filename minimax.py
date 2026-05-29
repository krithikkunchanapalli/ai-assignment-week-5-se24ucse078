# Minimax Algorithm

def minimax(depth, node_index, is_max, values, max_depth):

    if depth == max_depth:
        return values[node_index]

    if is_max:
        left = minimax(depth + 1, node_index * 2,
                       False, values, max_depth)

        right = minimax(depth + 1, node_index * 2 + 1,
                        False, values, max_depth)

        return max(left, right)

    else:
        left = minimax(depth + 1, node_index * 2,
                       True, values, max_depth)

        right = minimax(depth + 1, node_index * 2 + 1,
                        True, values, max_depth)

        return min(left, right)


values = [3, 5, 2, 9, 12, 5, 23, 23]

result = minimax(0, 0, True, values, 3)

print("Leaf Values:", values)
print("Best Value Found:", result)
