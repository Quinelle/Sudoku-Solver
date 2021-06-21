#sodoku solver that uses backtracing and recusion to solve also timed

board = [
    [0, 4, 0, 5, 0, 0, 8, 3, 0], 
    [0, 0, 0, 0, 8, 9, 5, 0, 1], 
    [8, 7, 5, 0, 6, 3, 4, 9, 0], 
    [0, 1, 0, 0, 0, 4, 3, 2, 0], 
    [2, 8, 0, 9, 3, 0, 6, 0, 0], 
    [7, 0, 0, 0, 0, 0, 9, 0, 0], 
    [0, 0, 0, 3, 0, 6, 0, 0, 0], 
    [4, 0, 0, 0, 0, 2, 0, 0, 9], 
    [0, 5, 2, 0, 9, 0, 0, 0, 0]
]
# prints out board given
import datetime
start_time = datetime.datetime.now()

def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# finds empty cell denoted by 0 to be used in solve function


def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)
    return None

# checks if the board is valid for use


def validation(board, num, pos):
    # checks row but not what was just placed
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
     # checks colmun but not what was just placed
    for i in range(len(board[0])):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    # checks boxes
    boxX = pos[1] // 3
    boxY = pos[0] // 3

    for i in range(boxY * 3, boxY * 3 + 3):
        for j in range(boxX * 3, boxX * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True
# if solution fails then it reset value to different then try again


def solve(board):
    # base case
    find = findEmpty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if validation(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False


printBoard(board)
solve(board)
end_time = datetime.datetime.now()
time = end_time - start_time
print("------Finished--------")
printBoard(board)
print("Time taken to solve: " + str(time))

