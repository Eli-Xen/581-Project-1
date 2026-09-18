# minesweeper.py
# author: Zachary McCauley

# use from minesweeper import Minesweeper

import random

class Minesweeper:
    def __init__(self, mines = 15):
        self.m = mines #determines how many mines are placed on board, default is 15
        self.flags = 0 #keeps tracked of how many flags are currently placed, may be used later to enforce a max flags
        self._digs = 100 - mines #used to determine if the player has won
        self.is_constructed = False
        self._internal = [[0 for i in range(10)] for j in range(10)]
        self._external = [[0 for i in range(10)] for j in range(10)]

    #method to generate board, called after player picks starting space
    #paramaters s_row and s_col are the row and column of the starting space
    def createBoard(self, s_row, s_col):
        c = 0
        while c < self.m:
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            if self._internal[row][col] < 0 or (row == s_row and col == s_col):
                pass
            else:
                self._internal[row][col] = -1
                for i in range(max(0, row - 1), min(10, row + 2)):
                    for j in range(max(0, col - 1), min(10, col + 2)):
                        if self._internal[i][j] != -1:
                            self._internal[i][j] += 1
                c += 1
        self.is_constructed = True
        self.dig(s_row, s_col)

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

    # Chord function, common in most minesweeper games.
    # Returns 2 - Does nothing if the number does not match the number of adjacent flags
    # Returns 1 - Progress was made
    # Returns 0 - The player lost
    def chord(self, row, col):
        # First, check if we are dealing with a revealed tile
        # If not, this function should do nothing
        displayVal = self.display(row, col)
        if displayVal <= 0:
            return 2
        # Check if number of flags matches number of adjacent positions
        flagCount = 0
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                # Use try statement so we can ignore checking for indexes
                if r < 0 or c < 0:
                    continue
                try:
                    if self.display(r, c) == 0:
                        flagCount += 1
                except IndexError:
                    # Do nothing; no need to check this out-of-bounds cell
                    pass
        # If chord values do not match, do nothing.
        if flagCount != displayVal:
            return 2
        # Dig all adjacent tiles
        toReturn = 1
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                # Use try statement so we can ignore checking for indexes
                try:
                    # To deal with negative indexing.
                    # A useful feature, just not here.
                    if r < 0 or c < 0:
                        continue
                    if self.display(r, c) == -3:
                        toReturn = 1 if self.dig(r, c) > 0 and toReturn == 1 else 0
                except IndexError:
                    # Do nothing; no need to check this out-of-bounds cell
                    pass
        return toReturn
        

    #method called to determine sprite used for specific cell
    #returns -3 if cell is still covered (sprites[0])
    #returns -2 if cell is a zero (sprites[1])
    #returns -1 if cell is a mine (sprites[2])
    #returns 0 if cell is flag (sprite[3])
    #returns 1-8 if cell is 1-8 (sprites[4] - sprites[11])
    #parameters are the row and column the sprite is for
    def display(self, row, col):
        cell = self._external[row][col]
        if cell == 2:
            #print(0)
            return 0 #flag
        elif cell == 1:
            if self._internal[row][col] == -1:
                #print(-1)
                return -1 #mine
            elif self._internal[row][col] == 0: 
                #print(-2)
                return -2 #zero
            else:
                #print(self._internal[row][col])
                return self._internal[row][col]
        else: #cell == 0
            #print(-3)
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