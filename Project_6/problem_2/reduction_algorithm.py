# a node class representing our literal
class Node:
    def __init__(self, literal, clause):
        self.literal = literal  # the identity of the literal.
        self.clause = clause  # the clause it belongs to
        self.boolean_value = None  # boolean value, not used for this task
        self.neighbours = []  # adjacent vertices.

    def add_neighbour(self, node):
        self.neighbours.append(node)


# graph of the nodes.
class Graph:
    def __init__(self):
        self.vertices = []
        self.size = None

    def find_size(self):
        self.size = len(self.vertices)

    def add_vertex(self, node):
        self.vertices.append(node)

    # create an adjacency matrix and then print it.
    def print_adjacency_matrix(self):
        adjacency_matrix = [['-' for i in range(self.size)] for j in range(self.size)]

        # add "inf" to the diagonal
        for i in range(self.size):
            adjacency_matrix[i][i] = "inf"
        # find adjacent vertices.
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if self.vertices[j] in self.vertices[i].neighbours:
                    adjacency_matrix[i][j] = 1
                    adjacency_matrix[j][i] = 1

        print(*adjacency_matrix, sep='\n')


# an example of a CNF
def logic_example():
    # each row is a clause
    CNF = ((1, 2), (-2, 4), (-1, 2))
    graph = reduce_to_clique_problem(CNF)
    graph.print_adjacency_matrix()


# turns each literal into vertices
def transform_to_vertices(CNF):
    graph = Graph()
    # goes through each clause and each literal inside the clause
    for index, clause in enumerate(CNF):
        for literal in clause:
            node = Node(literal, index)
            graph.add_vertex(node)

    graph.find_size()
    return graph


# creates the edges between the vertices in the undirected graph.
def create_edges(graph):
    # loop through the vertices in the graph,
    for i in range(graph.size):
        # vertices that have already been compared does not need to be compared a second time.
        for j in range(i + 1, graph.size):
            # checks if it is a valid edge
            if check_constraints(graph.vertices[i], graph.vertices[j]):
                graph.vertices[i].add_neighbour(graph.vertices[j])
                graph.vertices[j].add_neighbour(graph.vertices[i])
    return graph


def check_constraints(vertice_i, vertice_j):
    # if both are in the same clause return false
    if vertice_i.clause == vertice_j.clause:
        return False
    # if one of the literal is a negation of the other, return False
    if abs(vertice_i.literal) == abs(vertice_j.literal):
        if vertice_i.literal != vertice_j.literal:
            return False

    return True


# starts the reduction
def reduce_to_clique_problem(logic_expression):
    graph = transform_to_vertices(logic_expression)
    graph = create_edges(graph)
    return graph
