import extract_dataset
import generate_frequencies

class Node:
    def __init__(self, key, value, freq):
        self.key = key  # latitude
        self.value = value  # which city it is
        self.freq = freq

        self.left = None
        self.right = None

    def insert(self, key, value):
        self.key = key
        self.value = value


class BinaryTree:
    # function outside of binary tree builds it?
    def __init__(self, dataset):
        self.root = None
        self.nodes = []
        self.dataset = dataset
        #self.insert_many(dataset)
        self.optimalize()
        self.bfs()

    def search(self, key):
        cur_node = self.root

        while True:
            if cur_node.key == key:
                print(cur_node.value)
                cur_node.freq += 1
                self.optimalize()
                break

            elif cur_node.key > key:
                if cur_node.left:
                    cur_node = cur_node.left
                    continue
                else:
                    print(f"No city of latitiude {key} was found")
                    break

            elif cur_node.key < key:
                if cur_node.right:
                    cur_node = cur_node.right
                    continue
                else:
                    print(f"No city of latitiude {key} was found")
                    break

    def optimalize(self):
        n = len(self.dataset)

        cost = [[0 for i in range(n + 1)] for j in range(n + 1)]
        root_table = [[0 for i in range(n + 1)] for j in range(n + 1)]
        for i in range(n):
            cost[i][i + 1] = self.dataset[i][2]
            root_table[i][i + 1] = i + 1
        # last row is 154

        for l in range(2, n + 1):
            for k in range(0, n + 1 - l):
                cost[k][k + l], root_table[k][k + l] = self.find_cost(cost, root_table, k, k + l)
        root_table.pop(-1)
        [row.pop(0) for row in root_table]
        self.build_optimal_binary_tree(None, root_table, 0, n - 1)
        return

    def find_cost(self, cost, root_table, i, j):
        costs = []  # at the end find the min_cost of the costs in here
        root_value = []
        for n in range(i + 1, j + 1):
            costs.append(cost[i][n - 1] + cost[n][j])
            root_value.append(n)

        return sum(costs) + min(costs), root_table[root_value[costs.index(min(costs))] - 1][root_value[costs.index(min(costs))]]

    def build_optimal_binary_tree(self, prev_node, root_table, i, j):

        k = root_table[i][j] - 1
        cur_node = Node(self.dataset[k][1], self.dataset[k][0], self.dataset[k][2])
        """
        self.root = cur_node
        stack = []  # [node, i, j]
        stack.append([cur_node, i, j])
        while stack:
            prev_node, i, j = stack.pop(-1)
            if k == 0:
                continue
            if k < j:
                k = root_table[k + 1][j]
                cur_node = Node(self.dataset[k][1], self.dataset[k][0], self.dataset[k][2])
                prev_node.right = cur_node
                stack.append([cur_node, k + 1, j])
            if k > i:
                k = root_table[i][k - 1]
                cur_node = Node(self.dataset[k][1], self.dataset[k][0], self.dataset[k][2])
                prev_node.right = cur_node
                stack.append([cur_node, i, k - 1])
        """
        #"""
        if cur_node.value == 'Mandal':
            a = 1
        if k == -1:
            return
        if prev_node is None:
            self.root = cur_node
            self.nodes.append(cur_node.value)
            self.build_optimal_binary_tree(cur_node, root_table, k + 1, j)
            self.build_optimal_binary_tree(cur_node, root_table, i, k - 1)
        else:
            if k < j or True:
                if cur_node.key > prev_node.key:
                    prev_node.right = cur_node
                    self.nodes.append(cur_node.value + ' - right')

            if k > i or True:
                if cur_node.key < prev_node.key:
                    prev_node.left = cur_node
                    self.nodes.append(cur_node.value + ' - left')
            if k < len(root_table) - 1:
                self.build_optimal_binary_tree(cur_node, root_table, k + 1, j) #right
            if k > 0:
                self.build_optimal_binary_tree(cur_node, root_table, i, k - 1)

            #i suspect it doesn't add leaves

        #"""
        """
        k = root_table[i][j]
        cur_node = Node(self.dataset[k - 1][1], self.dataset[k - 1][0], self.dataset[k - 1][2])
        if j == k or k == 0:
            return
        if self.root is None:
            self.root = cur_node

        if i == j:
            if prev_node:
                if prev_node.key < cur_node.key:
                    prev_node.right = cur_node
                elif prev_node.key > cur_node.key:
                    prev_node.left = cur_node
        else:
            #split dataset in two halves.
            if prev_node:
                if prev_node.key < cur_node.key:
                    prev_node.right = cur_node
                elif prev_node.key > cur_node.key:
                    prev_node.left = cur_node

            self.build_optimal_binary_tree(cur_node, root_table, i, k)
            self.build_optimal_binary_tree(cur_node, root_table, k + 1, j)
        """



    def set_new_root_node(self):
        pass

    def bfs(self):
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            #self.nodes.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def build_tree(norwegian_cities):
    binary_tree = BinaryTree(norwegian_cities)
    return binary_tree


def interact(binary_tree):
    while True:
        latitude = input("Write the latitude: ")
        if latitude != 'done':
            # update frequencies if node found += 1
            binary_tree.search(latitude)
        else:
            break


def main():
    norwegian_cities = extract_dataset.open_file()
    norwegian_cities = generate_frequencies.generate_frequencies(norwegian_cities)
    binary_tree = build_tree(norwegian_cities)
    #binary_tree = generate_frequencies.generate_frequencies(binary_tree)
    #binary_tree.optimalize(norwegian_cities)
    bfs(binary_tree)
    interact(binary_tree)

def bfs(binary_tree):
    queue = [binary_tree.root]
    counter = 1
    city = []
    while queue:
        node = queue.pop(0)
        if node.value not in city:
            print(node.value, '--', counter)

            counter += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

if __name__ == "__main__":
   main()

