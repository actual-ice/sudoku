class sudoku_game():
    def __init__(self):
        self.__gameboard = random_game() # generate a list of numbers for a valid sudoku game
        main_loop() # start the game

    def make_move(self):
        move = get_move() # move = (xpos, ypos, move_input)
        if legal_move(move):
            self.__gameboard[move[0], move[1]] = move[2]

    def __main_loop():
        while True:
            if __legal_moves == 0:
                print("You Won!")
            else: 
                make_move()