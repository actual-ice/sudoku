from random import shuffle

class sudoku_game():
    def __init__(self):
        self.__gameboard = random_game() # generate a list of numbers for a valid sudoku game
        main_loop() # start the game

    def make_move(self):
        move = get_move() # move = (xpos, ypos, move_input)
        if legal_move(move):
            self.__gameboard[move[0], move[1]] = move[2]

    def random_game():
        moves = [1,2,3,4,5,6,7,8,9]
        game = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(9)]
        
        for row in range(len(game)):
            shuffle(moves) # shuffle the order of the moves to randomize
            
            for column in range(len(game[row])):
                for move in moves:
                    if legal_move(game, row, column, move):
                        game[row][column] = move
                        moves.remove(move) # remove the moves already made
                        break
            
            moves = [1,2,3,4,5,6,7,8,9] # form the moves list again for the next row

        return game

    def legal_move(game, row, column, move):
        """
        generates an array with 9 arrays, each with 9 numbers representing the game board
        """

        if move not in game[row]: # check the row

            if move not in [game[num][column] for num in range(len(game))]:

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

    def __main_loop():
        while True:
            if __legal_moves == 0:
                print("You Won!")
            else: 
                make_move()