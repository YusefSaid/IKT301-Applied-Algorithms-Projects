import random
def generate_frequencies(norwegian_cities):
    for city in norwegian_cities:
        city[2] = random.randint(0, 50)
    """
    queue = [binary_tree.root]
    counter = 1

    while queue:
        node = queue.pop(0)
        node.freq = random.randint(0, 50)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    #binary_tree.optimalize()
    """
    return norwegian_cities