import numpy as np

# global variables
visited_nodes = 0
promising_nodes = 0


def run_sudoku():
    M = initialize_sudoku_board()
    # M is the sudoku board, as an array with length 81, 0 is the first position on the sudoku board.
    solve_sudoku(M, 0, np.zeros((9, 81)))


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


def solve_sudoku(M, i, sudoku_list):
    fill_missing(M)


    # reshapes the array into a 9x9 matrix
    a = np.reshape(M, (9, 9))
    # the deductive solution will only run after 3 slots on the sudoku board has been filled or passed by
    # this is to improve performance as deductive strategies probably doesn't have to be run every time
    if i % 3 == 0:
        sudoku_list = deductive_strategies(M)

    global promising_nodes
    global visited_nodes
    visited_nodes += 1  # everytime the solve_sudoku function is invoked it means it is visiting a node.

    # reshape sudoku_list into a 9x9x9 tensor,
    # creating a 3-dimensional representation of the sudoku board
    # each depth shows a map of the sudoku board for a singel value (1-9) has an x-wing setup
    # for example sudoku_list[2] may have the matrix

    # [[0. 0. 3. 0. 0. 3. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
    #  [0. 0. 3. 0. 0. 3. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]]

    # which means that we have an x-wing for the value 3
    # that means it can only appear somewhere in those 4 positions,
    # any other places in those rows or columns are invalid for that value.

    sudoku_list = np.reshape(sudoku_list, (9, 9, 9))

    # checks if the last value in the board has been filled,
    # if yes then a solution has been found.
    # the program will continue to run after this,
    # and so if there are more solutions it will print them as well
    if i == len(M):
        print(np.reshape(M, (9, 9)))
        print("Visited nodes:", visited_nodes - 1)
        print("Promising nodes:", promising_nodes)



    # code starts looking for a number that fits in the slot if the slot is not filled in already
    elif M[i] == 0:
        for k in range(1, 10):
            visited_nodes += 1  # everytime the solve_sudoku function is invoked it means it is visiting a node.

            # check if k is a valid solution for the slot
            if check_solution(M, k, i):  # new row every 9th column for j
                a = i % 9
                b = int(i / 9)

                # check if there are any elements in the row or columns
                # of the number k to see if it fits with x-wing
                # if the sum of the row or column is 0 then x-wing does not apply,
                # if it does apply, then the slot where k is being placed must be one of the slots with the value
                # any other slots in the row or column ie the ones with 0 in them means the if statement is False
                if (np.sum(sudoku_list[k - 1][b][:]) == 0 and np.sum(sudoku_list[k - 1][:][a]) == 0) or \
                        sudoku_list[k - 1][b][a] == k:
                    # if the number is valid for that position on the sudoku it means it is a promising node
                    promising_nodes += 1
                    M[i] = k
                    solve_sudoku(M, i + 1, sudoku_list)

                    # if the solve_sudoku function returns,
                    # it means that it did not find a suitable number for the slot
                    # the slot is then set to 0
                    M[i] = 0

            # this will run if there is a slot that is already filled. so it moves on to the next slot
            else:
                continue

    # this will run if there is a slot that is already filled. so it moves on to the next slot
    else:
        solve_sudoku(M, i + 1, sudoku_list)


def deductive_strategies(M):
    # the deductive strategy used is a form of x-wing.
    # create a matrix, where 81 is the sudoku board flattened out
    sudoku_list = np.zeros((9, 81))

    # copy the list so that we dont have to alter it.
    # sudoku_list_cpy = np.zeros((9, 81))
    for i in range(len(M)):
        # if the value is 0 then the slot has already
        # been filled and the possible value there is already certain
        if M[i] != 0:
            continue
        else:
            for k in range(1, 10):
                if check_solution(M, k, i):
                    # fill the list with every possible number for that slot
                    sudoku_list[k - 1][i] = k
                    # sudoku_list_cpy[k - 1][i] = k

    # find if x-wing occurs, reshape into a 3 dimensional representation of the sudoku board.
    # the depth represents the possible values for each slot, 1-9
    sudoku_list = np.reshape(sudoku_list, (9, 9, 9))

    for m in range(9):
        # m represents the possible values for a slot

        for o in range(9):

            # if the sum of the column at depth m divided by the value m + 1 does not equal two,
            # then there are either more or less possible positions in the column for that particular value
            # meaning no x-wing
            if sum(sudoku_list[m][:, o]) / (m + 1) != 2:
                sudoku_list[m][:, o] = 0

        # this removes instances where there are not two of a value in a row
        # for example, this will remove the three at [2, 6] is removed
        # [[0. 0. 3. 0. 0. 3. 0. 0. 0.]   becomes  # [[0. 0. 3. 0. 0. 3. 0. 0. 0.]
        #  [0. 0. 0. 0. 0. 3. 0. 0. 0.]            #  [0. 0. 0. 0. 0. 3. 0. 0. 0.]
        #  [0. 0. 3. 0. 0. 0. 3. 0. 0.]            #  [0. 0. 3. 0. 0. 0. 0. 0. 0.]
        #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]            #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
        #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]            #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
        #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]            #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
        #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]            #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
        #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]            #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
        #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]]           #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]]

        for n in range(9):
            # if the sum of the row at depth m divided by the value m + 1 does not equal two,
            # then there are either more or less possible positions in the row for that particular value
            # meaning no x-wing
            if sum(sudoku_list[m][n, :]) / (m + 1) != 2:
                # remove the values from the list.
                sudoku_list[m][n, :] = 0
        # for example, this will remove the threes at [1, 5] and [2, 2]
        # [[0. 0. 3. 0. 0. 3. 0. 0. 0.]   becomes  # [[0. 0. 3. 0. 0. 3. 0. 0. 0.]
        #  [0. 0. 0. 0. 0. 3. 0. 0. 0.]            #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
        #  [0. 0. 3. 0. 0. 0. 0. 0. 0.]            #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
        #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]            #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
        #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]            #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
        #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]            #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
        #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]            #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
        #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]            #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
        #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]]           #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]]

        # a double check for columns is necessary as values may have been removed from the column during the row check
        for p in range(9):
            if sum(sudoku_list[m][:, p]) / (m + 1) == 1:
                sudoku_list[m][:, p] = 0

        # for example, this will remove the threes at [0, 2] and [0, 5]
    # [[0. 0. 3. 0. 0. 3. 0. 0. 0.]   becomes  # [[0. 0. 0. 0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]            #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]            #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]            #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]            #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]            #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]            #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]            #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]]           #  [0. 0. 0. 0. 0. 0. 0. 0. 0.]]

    sudoku_list = np.reshape(sudoku_list, (81, 9))
    return sudoku_list


def fill_missing(M):
    global visited_nodes
    global promising_nodes
    # if there are any slots that has only one possible value that can be inserted,
    # it will insert that value
    M = np.reshape(M, (81, 1))
    for i in range(len(M)):
        counter = 0
        a = 0
        if M[i] != 0:
            continue
        for k in range(1, 10):
            if check_solution(M, k, i):
                counter += 1
                a = k
                visited_nodes += 1
                promising_nodes += 1
        if counter == 1 and a != 0:
            M[i] = a
    return M


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
