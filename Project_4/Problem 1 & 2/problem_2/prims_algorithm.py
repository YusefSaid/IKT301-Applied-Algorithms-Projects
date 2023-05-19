def prim(A):
    tree = [[None for i in range(len(A))] for j in range(len(A))]
    # tree is represented as an adjacency matrix
    visited = [1]  # 1 is start node
    for i in range(len(tree)):
        tree[i][i] = 0

    while True:
        min_cost, next_node, prev_node = add_node(A, visited)
        if min_cost is None:
            break
        visited.append(next_node)
        tree[prev_node - 1][next_node - 1] = min_cost
        #tree[next_node - 1][prev_node - 1] = min_cost

    return tree


def add_node(A, visited):
    min_cost = float("inf")
    next_node = None
    prev_node = None
    for node in visited:
        for index, candidate in enumerate(A[node - 1]):
            if index + 1 in visited or candidate is None:
                continue
            elif candidate < min_cost:
                min_cost = candidate
                next_node = index + 1
                prev_node = node

    if next_node is None:
        return None, None, None
    else:
        return min_cost, next_node, prev_node
