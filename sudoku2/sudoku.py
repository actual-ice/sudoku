"""

This program generates a 9 by 9 grid of numbers to randomly generate finished sudoku boards
gen_rand() will produce a list of 9 lists, each containing 9 numbers

for example:
    print(gen_rand())
    output:
    [[9, 1, 2, 7, 3, 4, 6, 5, 8], [8, 7, 4, 6, 5, 2, 3, 1, 9], [5, 3, 6, 9, 1, 8, 2, 4, 7], [2, 8, 9, 1, 7, 3, 4, 6, 5],
    [7, 6, 1, 4, 8, 5, 9, 2, 3], [3, 4, 5, 2, 9, 6, 7, 8, 1], [6, 5, 8, 3, 2, 7, 1, 9, 4], [1, 2, 7, 5, 4, 9, 8, 3, 6], [4, 9, 3, 8, 6, 1, 5, 7, 2]]

you can use print_game() to print the output like an actual sudoku board

for example:
    print_game(gen_rand())
    output:
    [9, 1, 2, 7, 3, 4, 6, 5, 8]
    [8, 7, 4, 6, 5, 2, 3, 1, 9]
    [5, 3, 6, 9, 1, 8, 2, 4, 7]
    [2, 8, 9, 1, 7, 3, 4, 6, 5]
    [7, 6, 1, 4, 8, 5, 9, 2, 3]
    [3, 4, 5, 2, 9, 6, 7, 8, 1]
    [6, 5, 8, 3, 2, 7, 1, 9, 4]
    [1, 2, 7, 5, 4, 9, 8, 3, 6]
    [4, 9, 3, 8, 6, 1, 5, 7, 2]

however this program is far from perfect, in reality what the program is doing is attempting to generate the board, and
the output is not always correct, so the method i went for is to generate the board, and if it's not correct, generate another one,
until the output is viable.

but one thing is for sure, and that is that I, made this program without searching for algorithms to generate the board, but instead
attempted to create my own algorithm

of course this algorithm is, let's just say, hot garbage, but it's MY hot garbage
"""

# THE FIRST SUDOKU GAME SUCCESFULLY GENERATED
# 7/21/2021
# LETS GOOOOOOOOOOOOOOOOOOOOOOO

# [
# [3, 4, 5, 1, 2, 8, 7, 9, 6], 
# [8, 1, 2, 7, 9, 6, 4, 5, 3], 
# [7, 6, 9, 5, 3, 4, 2, 1, 8], 
# [9, 7, 3, 6, 1, 2, 5, 8, 4], 
# [1, 5, 6, 8, 4, 9, 3, 7, 2], 
# [4, 2, 8, 3, 7, 5, 9, 6, 1], 
# [6, 8, 7, 2, 5, 3, 1, 4, 9], 
# [2, 9, 1, 4, 6, 7, 8, 3, 5], 
# [5, 3, 4, 9, 8, 1, 6, 2, 7]
# ]



from random import shuffle
from random import randint
from copy import deepcopy

def random_game():
    game = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(9)] 

    for row in range(len(game)):
        if row in [0, 3, 6]:
            game[row] = random_frows(game, row)
        else:
            game[row] = random_mrows(game, row)  

    return game

def random_frows(game, row):
    """ 
    accepts game and row as input and returns randomly generated rows for row 0, 3, and 6 
    """
    moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    shuffle(moves)

    for column in range(9):
        for move in moves:
            if legal_move(game, row, column, move):
                game[row][column] = move
                moves.remove(move)
                break

    if game[row][8] == 0:
        game[row] = switch_moves(game, row, column, moves[0])
    
    return game[row]

def random_mrows(game, row):
    """
    accepts game and row as input and returns randomly generated rows for rows 1, 2, 4, 5, 7, 8
    """
    upper_row = deepcopy(game)
    upper_row = upper_row[row - 1]
    last_block = upper_row[6:9]

    shuffle(upper_row)
    shuffle(last_block)

    final_row = []

    first_block = [0,0,0]
    second_block = [0,0,0]
    third_block = [0,0,0]

    # first block
    for column in range(3):
        for move in upper_row:
            if legal_move(game, row, column, move):
                first_block[column] = move
                upper_row.remove(move)

                break

    # second block
    for column in range(3, 6):
        for move in last_block:
            if move in upper_row and legal_move(game, row, column, move):
                second_block[column - 3] = move
                upper_row.remove(move)

                break

    second_block_col = 3
    for i in second_block:
        if i == 0:
            for move in upper_row:
                if legal_move(game, row, second_block_col, move):
                    second_block[second_block_col - 3] = move
                    upper_row.remove(move)

                    break
                
        second_block_col += 1

    # third block

    for column in range(6, 9):
        for move in upper_row:
            if legal_move(game, row, column, move):
                third_block[column - 6] = move
                upper_row.remove(move)

                break

    final_row = [first_block, second_block, third_block]
    final_row = [inner for outer in final_row for inner in outer]

    if len(upper_row) == 1:
        for column in range(9):
            if final_row[column] == 0:
                game[row] = final_row
                final_row = switch_moves(game, row, column, upper_row[0])

                

    return final_row

def switch_moves(game, row, column, move):
    """
    accepts game, row, column, and move
    returns row with moves switched to make the row legal
    """

    for check_column in range(1, column + 1):
        check_move = game[row][column - check_column]

        # temp_game = game[:]
        temp = game[row][column]
        game[row][column] = 0
        game[row][column - check_column] = 0

        if legal_move(game, row, column - check_column, move) \
        and legal_move(game, row, column, check_move):
            
            game[row][column - check_column] = move
            game[row][column] = check_move
            return game[row]
            
            break
        
        else:
            game[row][column - check_column] = check_move
            game[row][column] = move

    return game[row]

def legal_move(game, row, column, move):
    """
    accepts game, row, column, and move as input
    returns False if move is not legal
    returns True if move is legal
    """

    if move not in game[row]: # check the row

        if move not in [game[num][column] for num in range(len(game))]: # should be for range(len(row))

            if row <= 2:

                if column <= 2:
                    sudoku_square = [i[0:3] for i in game[0:3]]
                    sudoku_square = [inner for outer in sudoku_square for inner in outer]
                    if move not in sudoku_square: # check the square
                        return True
                    else:
                        return False

                if column <= 5:
                    sudoku_square = [i[3:6] for i in game[0:3]]
                    sudoku_square = [inner for outer in sudoku_square for inner in outer]
                    if move not in sudoku_square: # check the square
                        return True
                    else:
                        return False

                if column <= 8:
                    sudoku_square = [i[6:9] for i in game[0:3]]
                    sudoku_square = [inner for outer in sudoku_square for inner in outer]
                    if move not in sudoku_square: # check the square
                        return True
                    else:
                        return False

            if row <= 5:

                if column <= 2:
                    sudoku_square = [i[0:3] for i in game[3:6]]
                    sudoku_square = [inner for outer in sudoku_square for inner in outer]
                    if move not in sudoku_square: # check the square
                        return True
                    else:
                        return False

                if column <= 5:
                    sudoku_square = [i[3:6] for i in game[3:6]]
                    sudoku_square = [inner for outer in sudoku_square for inner in outer]
                    if move not in sudoku_square: # check the square
                        return True
                    else:
                        return False

                if column <= 8:
                    sudoku_square = [i[6:9] for i in game[3:6]]
                    sudoku_square = [inner for outer in sudoku_square for inner in outer]
                    if move not in sudoku_square: # check the square
                        return True
                    else:
                        return False

            if row <= 8:

                if column <= 2:
                    sudoku_square = [i[0:3] for i in game[6:9]]
                    sudoku_square = [inner for outer in sudoku_square for inner in outer]
                    if move not in sudoku_square: # check the square
                        return True
                    else:
                        return False

                if column <= 5:
                    sudoku_square = [i[3:6] for i in game[6:9]]
                    sudoku_square = [inner for outer in sudoku_square for inner in outer]
                    if move not in sudoku_square: # check the square
                        return True
                    else:
                        return False

                if column <= 8:
                    sudoku_square = [i[6:9] for i in game[6:9]]
                    sudoku_square = [inner for outer in sudoku_square for inner in outer]
                    if move not in sudoku_square: # check the square
                        return True
                    else:
                        return False

        else: 
            return False
    
    else:
        return False

def gen_rand():
    while True:
        game = random_game()
        check = True
        for i in game:
            if 0 in i:
                check = False
                break
        if check == True:
            return game

def print_game(game):
    for i in game:
        print(i)

# driver code
if __name__ == "__main__":
    print_game(gen_rand())
    