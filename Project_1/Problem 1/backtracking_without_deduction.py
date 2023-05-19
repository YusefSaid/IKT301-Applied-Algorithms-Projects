import numpy as np

# Global variables
visited_nodes = 0
promising_nodes = 0


def run_sudoku():
    M = initialize_sudoku_board()
    # M is the sudoku board, as an array with length 81, 0 is the first position on the sudoku board.
    solve_sudoku(M, 0)


def initialize_sudoku_board():
    # create a 9x9 sudoku board, 0 means it is not yet filled

    # https: // www.websudoku.com /?level = 1 & set_id = 6013466563
    M = np.array([
        [4, 0, 6, 0, 0, 0, 0, 8, 0],
        [0, 1, 0, 3, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 6, 7, 3],
        [0, 6, 0, 1, 8, 3, 7, 0, 2],
        [3, 8, 0, 4, 0, 6, 0, 1, 9],
        [1, 0, 4, 9, 5, 7, 0, 6, 0],
        [5, 9, 1, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 1, 0, 3, 0],
        [0, 7, 0, 0, 0, 0, 8, 0, 1]]
    )


    # turns the 9x9 matrix into an array with 81 slots
    M = M.flatten()

    return M


def solve_sudoku(M, i):
    # makes sure that the variables invoked are the global ones
    global promising_nodes
    global visited_nodes

    # checks if the last value in the board has been filled,
    # if yes then a solution has been found.
    # the program will continue to run after this,
    # and so if there are more solutions it will print them as well
    if i == len(M):
        print(np.reshape(M, (9, 9)))
        print("Visited nodes:", visited_nodes)
        print("Promising nodes:", promising_nodes)


    # code starts looking for a number that fits in the slot if the slot is not filled in already
    elif M[i] == 0:
        for k in range(1, 10):
            visited_nodes += 1  # everytime the solve_sudoku function is invoked it means it is visiting a node.
            if check_solution(M, k, i):  # new row every 9th column for j
                # if the number is valid for that position on the sudoku it means it is a promising node
                promising_nodes += 1
                M[i] = k
                solve_sudoku(M, i + 1)
                # if the solve_sudoku function returns,
                # it means that it did not find a suitable number for the slot
                # the slot is then set to 0
                M[i] = 0

    # this will run if there is a slot that is already filled. so it moves on to the next slot
    else:
        solve_sudoku(M, i + 1)


def check_solution(M, k, i):
    j = i % 9  # finds the column in the matrix the number is placed
    i = int(i / 9)  # finds the row in the matrix the number is placed

    # turns the sudoku array back into a 9x9
    M = np.reshape(M, (9, 9))
    # checking vertical line for whether the number already exists
    for l in range(9):
        # if the value is at any point found it will return False meaning it is not a solution
        if k == M[l][j]:
            return False

    # checking horizontal line for whether the number already exists
    for m in range(9):
        # if the value is at any point found it will return False meaning it is not a solution
        if k == M[i][m]:
            return False

    # checking the box if the number is already present. that is, the 3x3 box
    # finding the upper leftmost slot in the 3x3 box
    x = int(i - i % 3)
    y = int(j - j % 3)

    # iterate through the 3 by 3 box
    for a in range(3):
        for b in range(3):
            if k == M[a + x][b + y]:
                # returns False if the number is already present.
                return False

    # if the code goes through all the above,
    # it means it does not conflict with any other values on the sudoku board,
    # and so returns True
    return True
