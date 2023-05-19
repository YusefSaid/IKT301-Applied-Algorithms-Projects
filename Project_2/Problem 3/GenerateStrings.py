import random
import numpy as np

def incidence_matrix():
    # weighted incidence graph where the value in the graph tells you the node it is going to or from,
    #assuming dashed lines are value 0 and complete lines are 1
    dfa = input("Which DFA? Type 1 or 2: ")

    if dfa == '2':
        I = np.array([
            [1, 3, 2, 5],
            [0, 4, 1, 6],

            [0, 1, 4, 7],
            [0, 2, 3, 8],

            [0, 7, 6, 1],
            [0, 8, 5, 2],

            [0, 5, 8, 3],
            [0, 6, 7, 4]
        ])
    else:
        I = [
            [0, 6, 7],
            [0, 10, 7],

            [0, 4, 4],
            [0, 10, 1],

            [1, 9, 3],
            [1, 6, 5],

            [1, 7, 10],
            [1, 2, 2],

            [0, 9, 1],
            [0, 8, 4]
        ]
    return I

def generate_string(I, length, string, node):

    while length != 0:
        num = random.randint(1, len(I[0]) - 1)
        if I[node][num] > 0:  # 0 is an empty move
            string.append(num - 1)
            node = I[node][num] - 1
            length -= 1

    string = "".join(map(str, string))
    label = I[node][0]
    return string, label

def strings(I):
    strings = []
    labels = []

    for i in range(100):
        max_length = 10 ** random.randint(1, 3)
        string, label = generate_string(I, length=random.randint(1, max_length), string=[], node=0)
        strings.append(string)
        labels.append(label)
    """
    for (string, label) in zip(strings, labels):
        print(string, '-', label)
    print(len(strings), '-', len(labels))
    """
    return strings, labels

