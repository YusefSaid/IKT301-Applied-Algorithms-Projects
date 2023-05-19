"""
import random


def find_path_costs(dataset):
    new_dataset = []
    for row in dataset:
        # change random with latitutde and lengtitude calculations later
        # create a 155 x 155 matrix that has all the possible paths.
        paths = [random.randint(1, 10) for i in range(5)]
        # paths.insert(0, row[0])
        new_dataset.append(paths)
        if row[0] == 'Kosvik':
            break
    new_dataset = [[0, 2, 9, float("inf")],
                   [1, 0, 6, 4],
                   [float("inf"), 7, 0, 8],
                   [6, 3, float("inf"), 0],
                   ]

    return new_dataset, 10

"""
#"""
import random
import math

def find_path_costs(dataset):
    value = 1 #int(input("Use subset of cities(1) or test(0)?"))

    if value != 0:
        length_of_dataset = 4
        city_list = []
        A = []
        for row in dataset:
            matrix_row = []
            for col in dataset:
                if row == col:
                    dst = 0
                else:
                    dst = round(math.sqrt(((float(row[1]) - float(col[1])) ** 2) + ((float(row[2]) - float(col[2])) ** 2)), 3)
                matrix_row.append(dst)
                if col[0] == dataset[length_of_dataset - 1][0]:
                    break
            A.append(matrix_row)

            city_list.append(row[0])

            if row[0] == dataset[length_of_dataset - 1][0]:
                break
    else:
        A = [[0, 1, 3, None, None],
             [1, 0, 3, 6, None],
             [3, 3, 0, 4, 2],
             [None, 6, 4, 0, 5],
             [None, None, 2, 5, 0],
            ]
        city_list = [None, None, None, None, None]

    return A, city_list
#"""