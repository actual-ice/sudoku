from random import shuffle
from random import randint

def random_game():
    moves = [1,2,3,4,5,6,7,8,9]
    game = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(9)]
    
    for row in range(len(game)):
        
        shuffle(moves) # shuffle the order of the moves to randomize
        
        if row in [0, 3, 6]:
            for column in range(len(game[row])):
                for move in moves:
                    if legal_move(game, row, column, move):
                        game[row][column] = move
                        moves.remove(move) # remove the moves already made
                        break
        
        else:

            block_config = block_assignment()
            if row in [1, 2]:
                game[row] = shuffle_row(block_config, 0, row, game)
            elif row in [4, 5]:
                game[row] = shuffle_row(block_config, 3, row, game)
            else:
                game[row] = shuffle_row(block_config, 6, row, game)


        moves = [1,2,3,4,5,6,7,8,9] # form the moves list again for the next row

    return game

def shuffle_row(block_config, game_row, curr_row, game):
    
    final_row = []

    first_block = game[game_row][0:3]
    second_block = game[game_row][3:6]
    third_block = game[game_row][6:9]

    shuffle(first_block)
    shuffle(second_block)
    shuffle(third_block)


    blocks = {1: first_block, 2:second_block, 3:third_block}
    row = [blocks[block_config[0][1]], blocks[block_config[1][1]], blocks[block_config[2][1]]]

    # column = 0
    # for block in row:
    #     for i in block:
    #         for move in block:
    #             if legal_move(game, curr_row, column, move):
    #                 final_row.append(i)
    #                 column += 1

    #                 break


    column = 0
    for block in row:
        checker = False

        column_save = column
        made_legal = 0
        while checker == False:
            shuffle(block)
            for move in block:
                if not legal_move(game, curr_row, column, move):
                    column = column_save
                    made_legal = 0
                    break
                else:
                    column += 1
                    made_legal += 1
            if made_legal == 3:
                checker = True
        final_row.append(block)

    

    return [inner for outer in final_row for inner in outer]

def block_assignment():
    ''' assign the blocks to be assigned to each other block '''
    game_blocks = [1, 2, 3]
    first_block = game_blocks[randint(1, 2)]

    if first_block == 2:
        second_block = 3
    else:
        second_block = 1

    if second_block == 3:
        third_block = 1
    else:
        third_block = 2

    return [(1, first_block), (2, second_block), (3, third_block)]

def legal_move(game, row, column, move):
    """
    generates an array with 9 arrays, each with 9 numbers representing the game board
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

print(random_game())