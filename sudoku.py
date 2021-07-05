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
        for row in len(game):
            for column in len(row):
                for move in moves:
                    if move not in game[row-1] \
                    and move not in [game[num-1][row] for num in row]: 
                        pass


    def __main_loop():
        while True:
            if __legal_moves == 0:
                print("You Won!")
            else: 
                make_move()