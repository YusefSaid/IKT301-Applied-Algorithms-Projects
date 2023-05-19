class Heap:
    def __init__(self):
        self.heap = []
        self.heapsize = len(self.heap)

    # insert a key at the available lowest leftmost end of the binary tree,
    # that is at the end of the heaplist.
    def insert(self, key):
        self.heap.append(key)
        self.heapsize = len(self.heap)
        self.bubble_up()

    # makes insertion of multiple keys easier.
    def insert_many(self, keys):
        if keys:
            for key in keys:
                self.insert(key)

    # when inserting a key, it is compared to the parent node,
    # if it is larger they will switch places. otherwise it nothing.
    # this will continue until it reaches the top of the tree, the first element in the list.
    def bubble_up(self):
        if self.heap:
            cur_node = self.heapsize - 1
            while cur_node != 0:  # ensures that it stops when it becomes the root node.
                # swap if parent node is smaller.
                if self.heap[cur_node] > self.heap[int((cur_node - 1) / 2)]:
                    self.swap(cur_node, int((cur_node - 1) / 2))
                    cur_node = int((cur_node - 1) / 2)
                    continue
                break

    # sift down the key value at the top, switch it with the child node that has the highest key value.
    # continue until the key value is higher than its child nodes.
    def sift_down(self):
        cur_node = 0
        # make sure it stops if it reaches the end of the heap
        while cur_node * 2 + 2 <= self.heapsize - 1:
            # chose the largest child key value of the parent node
            if self.heap[cur_node * 2 + 1] < self.heap[cur_node * 2 + 2]:
                # parent switches with the right child, if the parent is smaller
                if self.heap[cur_node] < self.heap[cur_node * 2 + 2]:
                    self.swap(cur_node, cur_node * 2 + 2)
                    cur_node = int(cur_node * 2 + 2)
                    continue
            else:
                # parent switches with the left child, if the parent is smaller
                if self.heap[cur_node] < self.heap[cur_node * 2 + 1]:
                    self.swap(cur_node, cur_node * 2 + 1)
                    cur_node = int(cur_node * 2 + 1)
                    continue
            # will stop if it is larger than any of the other values under it
            break

        # check if the left child exists, if it does, compare it with parent node.
        if cur_node * 2 + 1 == self.heapsize - 1:
            if self.heap[cur_node] < self.heap[cur_node * 2 + 1]:
                self.swap(cur_node, cur_node * 2 + 1)

    # swap the position of two nodes
    def swap(self, node_1, node_2):
        value_node_1 = self.heap[node_2]
        value_node_2 = self.heap[node_1]

        self.heap[node_2] = value_node_2
        self.heap[node_1] = value_node_1

    # when deleting the element at the top (the largest key value),
    # it is swapped with the element at the end of the heaptree.
    # then the heapsize is reduced by one, so that going forward it ignores the "deleted" values in the list.
    # then the new value at the top is sifted down.
    def heap_sort(self, keys):
        self.insert_many(keys)
        n = self.heapsize
        for i in range(n):
            self.swap(0, self.heapsize - 1)
            self.heapsize -= 1
            self.sift_down()
        return self.heap
