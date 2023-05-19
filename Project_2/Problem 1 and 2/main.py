import Problem_1
import Problem_2
import time
import numpy as np


def incidence_matrix():
    # weighted incidence graph where the value in the graph tells you the node it is going to or from,
    # assuming dashed lines are value 0 and complete lines are 1
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


def main():
    I = incidence_matrix()
    strings, labels = Problem_1.strings(I)
    a = time.time()
    Problem_2.GreedyApproach(strings, labels)
    b = time.time()
    print(f"Time: {b - a}")
if __name__ == "__main__":
    main()
