import random

class State:
    def __init__(self, w, h, no_mines):

        self.no_mines = no_mines
        self.w = w
        self.h = h


    def generate_board(self):
        self.board = [[0 for col in range(self.w)] for row in range(self.h)]
        for mine in range(self.no_mines):

            while True:
                row = random.randint(0, self.h-1)
                col = random.randint(0, self.w-1)
                if self.board[row][col] != -1
                    self.board[row][col] = -1
                    break
        
