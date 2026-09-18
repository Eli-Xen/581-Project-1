# minesweeper.py
# author: Zachary McCauley

# use from minesweeper import Minesweeper

import random

class Minesweeper:
    def __init__(self, mines = 15):
        self.m = mines #determines how many mines are placed on board, default is 15
        self.flags = 0 #keeps tracked of how many flags are currently placed, may be used later to enforce a max flags
        self._digs = 100 - mines #used to determine if the player has won
        self._internal = [[0 for i in range(10)] for j in range(10)]
        self._external = [[0 for i in range(10)] for j in range(10)]
        self.setUp = False

    #method to generate board, called after player picks starting space
    #paramaters s_row and s_col are the row and column of the starting space
    def createBoard(self, s_row, s_col):
        print("Creating minesweeper board...")
        # c is an iterator representing the number of placed mines
        c = 0
        while c < self.m:
            # Select a location to place the mine
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            # Pass if:
            #   A mine already exists at that location
            #   The location is where we selected
            if self._internal[row][col] < 0 or (row == s_row and col == s_col):
                pass
            else:
                # Mark that location as -1 (having a mine)
                self._internal[row][col] = -1
                # Increment all adjancent position's mine counts by 1.
                # ASSUMING no mine already exists at that location.
                for i in range(max(0, row - 1), min(10, row + 2)):
                    for j in range(max(0, col - 1), min(10, col + 2)):
                        if self._internal[i][j] != -1:
                            self._internal[i][j] += 1
                c += 1
        # Function to dig has been moved to click event in "UI Display.py"
        self.setUp = True

    #method called when player digs (left click) 
    #returns 2 if board didn't change (player dug at already uncovered space)
    #returns 1 if board was changed (player dug)
    #returns 0 if player dug mine (player lost)
    #parameters are the row and column the player digs at
    def dig(self, row, col):
        if self._external[row][col] != 0:
            return 2
        else:
            self._external[row][col] = 1
            if self._internal[row][col] == -1:
                return 0
            else:
                if self._internal[row][col] == 0:
                    for i in range(max(0, row - 1), min(10, row + 2)):
                        for j in range(max(0, col - 1), min(10, col + 2)):
                            self.dig(i, j)
                self._digs -= 1
                return 1

    #method called when player places flag (right click)
    #returns 2 if nothing happened (player tried to place flag on revealed tile)
    #returns 1 if a flag got removed
    #returns 0 if a flag was placed succesfully
    #parameters are the row and column player tries to place flag at
    def flag(self, row, col):
        if self._external[row][col] == 1:
            return 2
        elif self._external[row][col] == 2:
            self._external[row][col] = 0
            self.flags -= 1
            return 1
        else:
            self._external[row][col] = 2
            self.flags += 1
            return 0

    #method called to determine sprite used for specific cell
    #returns -3 if cell is still covered (sprites[0])
    #returns -2 if cell is a flag (sprites[3])
    #returns -1 if cell is a mine (sprites[2])
    #returns 0 if cell is 0 (sprite[1])
    #returns 1-8 if cell is 1-8 (sprites[4] - sprites[11])
    #parameters are the row and column the sprite is for
    def display(self, row, col):
        cell = self._external[row][col]
        if cell == 2:
            return -2 #flag
        elif cell == 1:
            if self._internal[row][col] == -1:
                return -1 #mine
            else: return self._internal[row][col]
        else: #cell == 0
            return -3 #covered

    #method to check if game is complete (player wins)
    #returns True if player won (game stops)
    #returns False otherwise (game continues)
    #method should be called everytime after the player digs
    #Note: returning false does not mean player lost
    def status(self):
        if self._digs == 0:
            return True
        else:
            return False

    #method to print internal board
    #used for testing purposes and should not be called by external code
    def _printB(self):
        for row in self._internal:
            print(row)