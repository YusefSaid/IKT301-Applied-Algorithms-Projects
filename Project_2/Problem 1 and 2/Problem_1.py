import numpy as np
import time


def generate_string(I, length, strings, string, labels, node):
    if length == -1:
        return strings, labels
    if len(string) != 0:
        labels.append(I[node][0])
        strings.append("".join(map(str, string)))

    for i in range(1, len(I[0])):
        if I[node][i] > 0:  # 0 is an empty move
            string.append(i - 1)
            pre_node = node
            node = I[node][i] - 1
            strings, labels = generate_string(I, length - 1, strings, string, labels, node)
            node = pre_node
            del string[-1]

    return strings, labels


def strings(I):
    l = int(input("Input string length: "))
    a = time.time()
    strings, labels = generate_string(I, length=l, strings=[], string=[], labels=[], node=0)
    b = time.time()
    print('Time:', b - a)
    # for (string, label) in zip(strings, labels):
    #   print(string, '-', label)
    # print(len(strings), '-', len(labels))
    return strings, labels
