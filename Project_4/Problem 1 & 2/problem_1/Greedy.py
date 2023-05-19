def greedy_algorithm(A, city_list):
    path = [1] #1 is start node
    cost = []
    while True:
        min_cost, next_node = find_local_optima(A[path[-1] - 1], path)
        if next_node == None:
            break

        path.append(next_node)
        cost.append(min_cost)
    print_path(path, cost, city_list)


def find_local_optima(row, path):
    min_cost = float("inf")
    next_node = None
    for index, node in enumerate(row):
        if index + 1 in path:
            continue
        if node < min_cost and node != 0:
            min_cost = node
            next_node = index + 1

    if next_node is None:
        return None, None
    return min_cost, next_node


def print_path(path, cost, city_list):
    print('Node: ', end="")
    for i in range(len(path)):
        print(city_list[path[i] - 1], end="-")

    print("")
    print('Cost: ', end="")

    for i in range(len(cost)):
        print(cost[i], end="-")
    print("")
    print('Total cost:', round(sum(cost), 1))
# the algorithm as written here,
# takes into account that all nodes can be reached from all other nodes.
