#Import numpy for array manipulation
import numpy as np

# magnets = ['+', '-', 'L', 'R', 'T', 'B']
# + = 1, - = -1 L = 2, R = 3, T = 4 and B = 5

magnets = np.array([1, -1, 2, 3, 4, 5])
# Limitations for +
top = [1, 10, 10, 2, 1, 10]
left = [2, 3, 10, 10, 10]

# Limitations for -
bottom = [2, 10, 10, 2, 10, 3]
right = [10, 10, 10, 1, 10]

# Board structure

# rules = [["L", "R", "L", "R", "T", "T"],
#        ["L", "R", "L", "R", "B", "B"],
#        ["T", "T", "T", "T", "L", "R"],
#       ["B", "B", "B", "B", "T", "T"],
#       ["L", "R", "L", "R", "B", "B"]]



#Define array with ints for further manipulation with numpy
#L = 2, R = 3, T = 4 and B = 5
rules = np.array([[2, 3, 2, 3, 4, 4],
                  [2, 3, 2, 3, 5, 5],
                  [4, 4, 4, 4, 2, 3],
                  [5, 5, 5, 5, 4, 4],
                  [2, 3, 2, 3, 5, 5]])

#Global variables for node counting
nodesVisited = 0
promisingNodesVisited = 0


#Simple loop for conversion of ints back to +, - and v (visited) characters
def convert(board):

    result = [["L", "R", "L", "R", "T", "T"],
            ["L", "R", "L", "R", "B", "B"],
            ["T", "T", "T", "T", "L", "R"],
            ["B", "B", "B", "B", "T", "T"],
            ["L", "R", "L", "R", "B", "B"]]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                result[i][j] = "+"

            if board[i][j] == -1:
                result[i][j] = "-"

            elif board[i][j] != 1 and board[i][j] != -1:
                result[i][j] = "v"

        print(result[i])


def solve_magnets(board, counter, row, col):
    global magnets
    global nodesVisited
    global promisingNodesVisited

    #Check if counter has reached the final element of the board
    if counter == len(board[0][:]) * len(board[:]):
        if final_check(board):
            return
        print("\n")
        print("Solution:")
        convert(board)
        print("\n")
        print("Total nodes visited: ", nodesVisited)
        print("Promising nodes visited: ",promisingNodesVisited)

    #If the board element is visited and is not 0 as in default, we perform another another check for alternative
    #magnet placement to satisfy our constrains, as well as add another visited/promising node as we are moving towards
    # solution

    elif board[row][col] != 0:
        counter += 1
        nodesVisited += 1
        promisingNodesVisited += 1
        solve_magnets(board, counter, int(counter / 6), counter % 6)

    else:
        #place +,-,2(L),3(R),4(T),5(B) can be places at he current position
        for item in magnets:
            board[row][col] = item
            nodesVisited +=1

            #check if the placement doest not brake any constraints
            if check_solution(board, row, col):
                counter += 1
                promisingNodesVisited+=1

                #As we confirm that constrains for board rules after placement are not broken we continue
                #to move to next column
                board, counter = add_values(board, row, col, counter)
                solve_magnets(board, counter, int(counter / 6), counter % 6)
                counter -= 1
                board[row][col] = 0
                if col != 5:
                    board[row][col + 1] = 0
                if row != 4:
                    board[row + 1][col] = 0
        board[row][col] = 0


def add_values(board, row, col, counter):
    global rules, nodesVisited, promisingNodesVisited

    #Via heuristic approach, we manage to try magnet placement on two positions L and R.
    #If placement is succesfull, we add values to visited and promising nodes.

    if (board[row][col] == 1 or board[row][col] == -1) and rules[row][col] == 2:
        board[row][col + 1] = board[row][col] * -1
        nodesVisited += 1
        promisingNodesVisited += 1
        counter += 1

    #The same placement only for T and B situation
    elif (board[row][col] == 1 or board[row][col] == -1) and rules[row][col] == 4:
        board[row + 1][col] = board[row][col] * -1

    #If it is not possible to place a L and R magnet we leave them empty and hop to next column
    elif board[row][col] == 2:
        board[row][col + 1] = 3
        counter += 1
        nodesVisited += 1
        promisingNodesVisited += 1

    #If it is not possible to place a T and B magnet we leave them empty and hop to next column
    elif board[row][col] == 4:
        board[row + 1][col] = 5

    return board, counter



#check if top,left,bottom,right constraint are not broken by current count of characters on board
#as well as run a check if a placed magnet does contain a charge which would hinder a placemnt of a new magnet
def check_solution(board, row, col):
    global top
    global left
    global bottom
    global right
    global rules

    #Check if current magnet placement is not constrained by character restriction on specific column.
    if top[col] < np.count_nonzero(board[:, col] == 1) or bottom[col] < np.count_nonzero(board[:, col] == -1):
        return False

    # Check if current magnet placement is not constrained by character restriction on specific row.
    if left[row] < np.count_nonzero(board[row, :] == 1) or right[row] < np.count_nonzero(board[row, :] == -1):
        return False


    # Check if the surrounding values holds the charge
    # x-dir -1 +1,
    # y-dir -1 +1
    # if there is one of the same value, return false.

    #Checks if not on the first row to avoid out of reach element error
    # Checks for magnet placement constrains, if there are any problems with matching charges in the same column.
    # T=4, B=5
    if row != 0:
        if board[row][col] == board[row - 1][col] and (board[row][col] == 1 or board[row][col] == -1):
            return False
        if board[row][col] != 5 and board[row - 1][col] == 4:
            return False
        if board[row][col] == 5 and board[row - 1][col] != 4:
            return False

    # Checks if not on the first column to avoid out of reach element error
    # Checks for magnet placement constrains, if there are any problems with matching charges on the same row.
    # L=2, R=3
    if col != 0:
        if board[row][col] == board[row][col - 1] and (board[row][col] == 1 or board[row][col] == -1):
            return False
        if board[row][col] != 3 and board[row][col - 1] == 2:
            return False
        if board[row][col] == 3 and board[row][col - 1] != 2:
            return False

    #Check if program has not reached the final row of the array.
    #Then checks if there are not matching charges on a row below.
    if row + 1 != len(board):
        if board[row][col] == board[row + 1][col]:
            return False

    # Check if program has not reached the final column of the row.
    # Then checks if there are not matching charges column to the right.
    if col + 1 != len(board[0]):
        if board[row][col] == board[row][col + 1]:
            return False


    # if the element is in B check above for a value being present,
    # if the element is in R check left if a value is present.
    # if not return false
    if board[row][col] != 1 and board[row][col] != -1:
        if board[row][col] != rules[row][col]:
            return False


    return True

#This final check looks up the constraints for board based on values specified in top,left,bottom, right arrays,
#Checks if total character count constraint per row and per column is satisfied
#Check occurs while being on final ellement of the array in this case it is row 5 element 6, board[4][5]
def final_check(board):
    for i in range(len(board[0])):
        if top[i] != 10:
            if top[i] != np.count_nonzero(board[:, i] == 1):
                return True
        if bottom[i] != 10:
            if bottom[i] != np.count_nonzero(board[:, i] == -1):
                return True

    for j in range(len(board)):
        if left[j] != 10:
            if left[j] != np.count_nonzero(board[j, :] == 1):
                return True
        if right[j] != 10:
            if right[j] != np.count_nonzero(board[j, :] == -1):
                return True
    return False


#Define initial board parameters and run the drivecode.
def main():
    board = [['0', '0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0', '0'],
             ]
    board = np.zeros((5, 6))
    solve_magnets(board, counter=0, row=0, col=0)



if __name__ == '__main__':
    main()