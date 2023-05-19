def kruskal(A):
    n = len(A)
    tree = create_adjacency_matrix(n)
    # tree is represented as an adjacency matrix


    list_of_edges = get_edge_list(A)
    total_edges = 0
    node_set = [[1]]
    for edge in list_of_edges:

        edge_status = check_sets(node_set, edge)
        if edge_status[0] is None and edge_status[1] is None:
            node_set.append([edge[0], edge[1]])

        elif edge_status[0] == edge_status[1]:
            continue

        elif edge_status[0] is None and edge_status[1] is not None:
            node_set[edge_status[1]].append(edge[0])

        elif edge_status[0] is not None and edge_status[1] is None:
            node_set[edge_status[0]].append(edge[1])

        elif edge_status[0] is not None and edge_status[1] is not None:
            node_set[edge_status[0]] += node_set[edge_status[1]]
            del node_set[edge_status[1]]

        tree[edge[0] - 1][edge[1] - 1] = edge[-1]
        tree[edge[1] - 1][edge[0] - 1] = edge[-1]
        total_edges += 1
        if total_edges == len(tree) - 1:
            break

    directed_tree = create_adjacency_matrix(n)
    tree, visited_nodes = turn_into_directed_graph(tree, tree[0], directed_tree, 0, [0])
    return tree


def check_sets(node_set, edge):
    edge_status = [None, None]

    for i in range(len(node_set)):
        for j in range(len(edge_status)):
            if edge[j] in node_set[i]:
                edge_status[j] = i

    return edge_status
def create_adjacency_matrix(n):
    A = [[None for i in range(n)] for j in range(n)]
    for i in range(n):
        A[i][i] = 0
    return A

def get_edge_list(A):
    list_of_edges = []  # start node, end node, edge value
    for index_start, node in enumerate(A):
        for index_end, edge in enumerate(node):
            if edge is None or index_start == index_end:
                continue
            if [index_end + 1, index_start + 1, edge] in list_of_edges:
                continue
            edge = [index_start + 1, index_end + 1, edge]
            list_of_edges.append(edge)
    return sorted(list_of_edges, key=lambda x: x[-1])


def turn_into_directed_graph(tree, node, directed_tree, row, visited_nodes):
    for i in range(len(node)):
        if node[i] != 0 and node[i] is not None:
            if i not in visited_nodes:
                directed_tree[row][i] = node[i]
                visited_nodes.append(i)
                directed_tree, visited_nodes = turn_into_directed_graph(tree, tree[i], directed_tree, i, visited_nodes)
    return directed_tree, visited_nodes