import random

class State:
    def __init__(self, w, h, no_mines):

        self.no_mines = no_mines
        self.w = w
        self.h = h
        self.generate_board()


    def generate_board(self):
        self.board = [[0 for col in range(self.w)] for row in range(self.h)]
        for mine in range(self.no_mines):

            while True:
                row = random.randint(0, self.h-1)
                col = random.randint(0, self.w-1)
                if self.board[row][col] != -1:
                    self.board[row][col] = -1                                            
                    break

        for row in range(self.h):
            for col in range(self.w):
                if self.board[row][col] != -1:
                    self.board[row][col] = self.count_mines(row,col)
        

                
    def count_mines(self, row, col):
        neighbouring_mines = 0
        
        #Check left hand side
        if row > 0:
            if self.board[row-1][col] == -1:
                neighbouring_mines += 1
            if col > 0:
                if self.board[row-1][col-1] == -1:
                    neighbouring_mines += 1
            if col < self.h-1:
                if self.board[row-1][col+1] == -1:
                    neighbouring_mines += 1

        #Check right hand side
        if row < self.w-1:
            if self.board[row+1][col] == -1:
                neighbouring_mines += 1
            if col > 0:
                if self.board[row+1][col-1] == -1:
                    neighbouring_mines += 1
            if col < self.h-1:
                if self.board[row+1][col+1] == -1:
                    neighbouring_mines += 1

        #check top
        if col > 0:
            if self.board[row][col-1] == -1:
                neighbouring_mines += 1

        #check bottom
        if col < self.h -1:
            if self.board[row][col+1] == -1:
                neighbouring_mines += 1

        return neighbouring_mines

