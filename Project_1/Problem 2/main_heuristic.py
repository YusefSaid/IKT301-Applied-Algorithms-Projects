# Problem 2
import random
import numpy as np

visited_nodes = 0
promising_nodes = 0


# 2.1 - Implement a backtracking solution.
def knight_tour(n):
    board = [[-1 for i in range(n)] for j in range(n)]

    # Theory of odd and even board sizes. (Explained more thoroughly further down)
    # For boards of odd order, such as 5x5 or 7x7,
    # solutions exist only for starting points whose coordinates total to an even number.

    # n + n = odd number    Solution Doesn't Exists
    # n + n = even number   Solution Exists

    knight_tour_helper(n=n, board=board, x=random.randint(0,n-1), y=random.randint(0,n-1), counter=1)
    print(np.array(board))


def knight_tour_helper(n, board, x, y, counter):
    global promising_nodes
    global visited_nodes
    position = find_next_valid_moves(x, y, n, board)
    finished = np.where(np.array(board) == -1)
    if len(finished[0]) < 1:
        print(np.array(board))
        print(f"Visited nodes   : {visited_nodes - 1:,}")
        print(f"Promising nodes : {promising_nodes:,}")
        exit(0)  # exits function

    if counter == (n * n) + 1:  # The game is won when all the squares have been visited.
                                    # We calculate the amount of squares by n*n
                                    # and we add a +1, because the counter starts at 1, and not 0. (See Task. 3.2)
        return True



    # If the x and y positions are invalid (Outside of board), or that the square has been visited. The move is illegal
    # Every square is created with the value "-1", and later on, changed with the current move number, to indicate the path.
    if (x < 0) or (x >= n) or (y < 0) or (y >= n) or board[y][x] != -1:
        return False

    # We mark the visited squares with counter, so that we know we've been there. [ Also it's task 3.3c-d ]
    board[y][x] = counter

    # The knight is moved through the following method:
    # X-axis direction and y-axis direction are stored as a tuple. 'Zip' is used to define all legal moves.(-2, -1) etc.
    # We call 'knight_tour_helper' recursively, to navigate to the next square, again and again
    # If all the legal moves have been made and it doesn't result in a Win. We Backtrack
    if len(position) > 0:
        visited_nodes += 1
        #promising_nodes += 1
        knight_tour_helper(n, board, position[1], position[0], counter + 1)
        promising_nodes += 1
        visited_nodes -= 1

    for x_move, y_move in zip([-2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, -2, 2, -2, 2, -1, 1]):
        visited_nodes += 1
        if knight_tour_helper(n, board, x + x_move, y + y_move, counter + 1):
            # If the move is valid, we add it to the promising nodes.
            #promising_nodes += 1
            return True

    # Backtracking.
    # When facing a dead end
    # we reassign the square as an unvisited one, thus trying a different approach.
    board[y][x] = -1
    return False


def find_next_valid_moves(x, y, n, board):
    possible_moves = np.zeros((n, n))
    if (x < 0) or (x >= n) or (y < 0) or (y >= n) or board[y][x] != -1:
        return

    possible_moves[y][x] = 99  # just marking the position of the last knight place
    for x_move, y_move in zip([-2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, -2, 2, -2, 2, -1, 1]):
        ax = x + x_move
        by = y + y_move

        if (ax < 0) or (ax >= n) or (by < 0) or (by >= n) or board[by][ax] != -1:
            continue
        for xx_move, yy_move in zip([-2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, -2, 2, -2, 2, -1, 1]):
            cx = ax + xx_move
            dy = by + yy_move

            if (cx < 0) or (cx >= n) or (dy < 0) or (dy >= n) or possible_moves[dy][cx] == 99:
                continue
            possible_moves[by][ax] += 1

    possible_moves[possible_moves == 0] = 99
    min = np.min(possible_moves)
    position = np.array(np.where(min == possible_moves))
    position = np.array((position[0][0], position[1][0]))

    return position


if __name__ == '__main__':
    knight_tour(6)  # Choose size of board: n x n

# To verify for yourself. Check link below
# /http://www.maths-resources.com/knights/



"""
As mentioned above, if the board size consists of an odd number, such as 5x5 or 7x7 etc. 
Then there exists a solution only for the starting positions, whose coordinates totals to an even number. 
If the starting position is e.g. x=1 and y=2. It totals to 1+2 = 3, which is an odd number. So for this
board size and starting position, there exists no solution. 

Note: This occurs because of the game structure itself.  

"""



