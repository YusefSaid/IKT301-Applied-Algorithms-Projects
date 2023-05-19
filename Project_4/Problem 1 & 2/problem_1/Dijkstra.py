def solve_with_dijkstra(A, city_list):
    costs = [float("inf") for i in range(len(A))]
    node = 0
    visited_nodes = [node]
    path = [node]
    paths = [0 for i in range(len(A))]

    min_cost  = float("inf")
    solve(A, node, path=[node], visited_nodes=[node], costs=costs, cost="inf")
    """
    for node in range(len(A)):
        for i in range(len(A)):
            if A[node][i] != 0 and A[node][i] not in path and A[node][i] != None:
                cur_cost = costs[node] + A[node][i]
                min_cost = min(costs)
                
                if cur_cost <= min_cost:
                    path.append(i)
                    del paths[node]
                    paths.insert(node, path)

                else:
                    path = paths[costs.index(min_cost)]

    """



def solve(A, node, path, visited_nodes, costs, cost):
    costs[node] += cost

    if len(path) == len(A):
        print(path, costs[node])

    for i in range(len(A)):
        if A[node][i] != 0 and A[node][i] is not None and i not in path:
            cost = costs[node] + A[node][i]
            if cost < costs[node]:
                pass

def minimum_cost():
    min_cost = float("inf")
    for i in range(3):
        pass