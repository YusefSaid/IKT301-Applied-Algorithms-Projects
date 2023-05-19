import numpy as np


class Node:
    def __init__(self):
        self.label = None
        self.paths = []  # list of input strings that have been added
        self.children = []
        self.source_edge = None
        self.source_node = None
        self.identifier = None
        self.string = None

        # if it reaches the end of the tree, but the string has not finished start inserting values

    def insert(self, char, counter):
        if char:
            if char not in self.paths:
                self.paths.append(char)
                self.children.append(Node())
                self.children[-1].source_edge = char
                self.children[-1].source_node = self
                self.children[-1].identifier = counter

    def set_label(self, label):
        if label:
            self.label = label

    def string(self, string):
        string = list(string)


class Tree:

    def __init__(self, strings, label):
        self.root = Node()
        self.root.label = 0
        self.root.identifier = 1
        self.build_tree(strings, label)
        self.tree = []

    def build_tree(self, strings, labels):
        node = self.root
        counter = 1
        # start in root node.
        for string, label in zip(strings, labels):
            node = self.root
            last_char = None
            string = list(string)
            for index_1, char in enumerate(string):

                if len(node.children) != 0:
                    for index, path in enumerate(node.paths):
                        if char == path:
                            node = node.children[index]
                            if index_1 == len(string) - 1:
                                node.label = label
                                node.string = "".join(string)

                        else:
                            counter += 1
                            node.insert(char, counter)
                            node = node.children[-1]
                            last_char = char
                            break
                else:
                    counter += 1
                    node.insert(char, counter)
                    node = node.children[0]
                    last_char = char

            if last_char is not None:
                node.label = label
                node.string = "".join(string)

    def breadth_first_search_tree(self):
        queue = []
        queue.append(self.root)
        while queue:
            node = queue.pop(0)
            # print(node.identifier)
            self.tree.append(node)
            for sub_node in node.children:
                queue.append(sub_node)


class Graph:
    def __init__(self, tree):
        self.root = tree.root
        self.graph = []
        self.graph.append(self.root)
        self.adjacency_matrix = None
        self.final_graph = []

    def insert(self, parent_node, sub_node):
        parent_node.children.append(sub_node)
        for index, source in enumerate(sub_node.source_node.paths):
            if sub_node.source_edge == source:
                del sub_node.source_node.children[index]
                break
        sub_node.source_node = parent_node

    def Merge_States(self, unique_node, sub_node):
        # paths_taken_that_leads_back_to_unique is a list of lists
        # merges nodes from subtree, we already know they can be merged

        # this one takes the node prior to the node being checked,
        # and make sure that when the subnode is being merged with unique,
        # that this one will now point to the unique node.
        if sub_node.source_node:
            for index, node in enumerate(sub_node.source_node.children):
                if node.identifier == sub_node.identifier:
                    del sub_node.source_node.children[index]
                    del sub_node.source_node.paths[index]
                    break
            #if unique_node not in sub_node.source_node.children:
            sub_node.source_node.children.append(unique_node)
            sub_node.source_node.paths.append(sub_node.source_edge)

    def build_adjacency_matrix(self):
        self.breadth_first_search()
        a = self.final_graph
        A = []
        for k in range(len(a)):
            arr = []
            for l in range(len(a) + 1):
                arr.append('-')
            A.append(arr)

        for index_1, node in enumerate(self.final_graph):
            # for index_2, subnode in enumerate(self.graph):
            A[index_1][0] = str(node.label)
            for i, sub_node in enumerate(node.children):
                if sub_node in self.final_graph:
                    index_2 = self.final_graph.index(sub_node)
                    if A[index_1][index_2 + 1] != '-':
                        A[index_1][index_2 + 1] = '(' + A[index_1][index_2 + 1] + ', ' + node.paths[i] + ')'
                    else:
                        A[index_1][index_2 + 1] = node.paths[i]
        # print(*A, sep='\n')
        # exit(0)
        self.adjacency_matrix = A

    def breadth_first_search(self):  # it needs to account for visited nodes, since its a graph
        queue = []
        queue.append(self.root)
        a = self.final_graph
        i= 0
        while queue:
            node = queue.pop(0)
            self.final_graph.append(node)
            for sub_node in node.children:
                #print(i)
                if sub_node in self.final_graph:
                    break
                else:
                    queue.append(sub_node)
        self.final_graph.pop()


def BuildPrefixTree(strings, labels):
    # construct the node labels from the generated trees.
    #strings = ['0', '00', '000', '001', '01', '010', '011', '1', '10', '100', '101', '11', '110', '111']
    #strings.reverse()
    #labels = [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    #labels.reverse()
    prefix_tree = Tree(strings, labels)
    queue = []
    queue.append(prefix_tree.root)
    identifier = 1
    # ordering the tree so that its easier to see which node is which
    while queue:
        node = queue.pop(0)
        node.identifier = identifier
        identifier += 1
        #print(node.identifier, '--', node.label, '--', node.string)
        for sub_node in node.children:
            queue.append(sub_node)
    prefix_tree.breadth_first_search_tree()
    Trachtenbrot_Barzdin_algorithm(prefix_tree)
    return prefix_tree


def breadth_first_search_graph(graph, unique_nodes):
    # do a breadth first search of the subtree, output which path it uses and use that for the unique tree and the label of the values they gets to and
    queue = []
    graphs = []
    identifiers = []
    queue.append(graph.root)
    graphs.append(graph.root)
    identifiers.append(graph.root.identifier)

    while queue:
        merged = 0
        node = queue.pop(0)
        for unique_node in unique_nodes:
            if node.label == unique_node.label and node.identifier not in identifiers:
                if MatchLabels(node, unique_node):
                    graph.Merge_States(unique_node, node)
                    merged = 1
                    break

        unique_nodes.append(node)
        identifiers.append(node.identifier)

        if merged == 0:
            for index, sub_node in enumerate(node.children):
                if sub_node not in graphs:
                    queue.append(sub_node)
                    graphs.append(sub_node)

        #graph.final_graph = unique_nodes
    #adjacency_matrix(unique_nodes)
def adjacency_matrix(unique_nodes):
    pass
def Trachtenbrot_Barzdin_algorithm(prefix_tree):
    prefix_tree.breadth_first_search_tree()

    graph = Graph(prefix_tree)
    unique_nodes = []
    unique_nodes.append(graph.root)
    breadth_first_search_graph(graph, unique_nodes)
    graph.build_adjacency_matrix()
    print(*graph.adjacency_matrix, sep='\n')


def MatchLabels(potential_node, unique_node):
    if potential_node.label != unique_node.label:
        #print(f'False {potential_node.label} -- {unique_node.label}')
        return False
    if len(potential_node.children) == 0:
        return True

    for index, sub_node in enumerate(potential_node.children):

        if potential_node.paths[index] not in unique_node.paths:
            return False
        #print(unique_node.paths.index(potential_node.paths[index]))
        i = unique_node.paths.index(potential_node.paths[index])  # so that they traverse identically
        #print(f"{potential_node.paths[index]} -- {unique_node.paths[i]}")
        if MatchLabels(potential_node.children[index], unique_node.children[i]) is False:
            #print(f'False')
            return False

    return True


def MergeStates(i, j, Node):
    # Merge the node pair i and j
    pass


def GreedyApproach(strings, labels):
    prefix_tree = BuildPrefixTree(strings, labels)
    pass
