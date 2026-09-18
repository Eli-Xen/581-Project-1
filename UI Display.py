# pip install pygame-ce --pre
# required for use

# prologue
# external sources: https://www.pygame.org/docs/
# author: Emilia Davis

import pygame
from minesweeper import Minesweeper

pygame.init()

board_size = 160 # base board size
label_size = 16 # base label size
square_size = 16 # base square size
board_scale = 4 # change scale of board

# load font comic sans
font = pygame.font.SysFont("Comic Sans MS", 8 * board_scale)

# load screen with given dimensions
screen = pygame.display.set_mode(((board_size + label_size) * board_scale, (board_size + label_size) * board_scale))

# load sprite sheet and create list of sprites
surface = pygame.image.load("SpriteSheet.png").convert()
sprites = []
# for every sprite in the sheet
for i in range(12):
    # find the area where the sprite sits
    sprite = surface.subsurface((i * 16, 0, 16, 16))
    # scale the sprite to fit the board
    sprite = pygame.transform.scale(sprite, (square_size * board_scale, square_size * board_scale))
    # add the sprite to the list of sprites
    sprites.append(sprite)

# Create reference to global variable board, used in showBoard.
# This should be later moved into a class, because global variables are ugly.
board = None

# displays board
def showBoard(surface):
    for row in range(10):
        for col in range(10):
            # draw sprite onto surface at given position
            # Choose which sprite to show
            # 0 - Unselected space
            # 1 - Space with no adjacent mines
            # 2 - Mine
            # 3 - Flag
            # 4-11 - Revealed space; values 1-8
            selectedSprite = None
            if board is None:
                raise RuntimeError("Board should be defined before calling showBoard!")
            displayOutput = board.display(row, col)
            match displayOutput:
                case -3:
                    # Covered cell
                    selectedSprite = 0
                case -2:
                    selectedSprite = 3
                case -1:
                    selectedSprite = 2
                case 0:
                    selectedSprite = 1
                case _:
                    selectedSprite = displayOutput + 3

            surface.blit(sprites[selectedSprite], (col * square_size * board_scale + label_size * board_scale, row * square_size * board_scale + label_size * board_scale)) # TODO: right now this just draws the covered sprite for every position, needs logic to determine what sprite to use

    # create labels for rows 1 - 10
    for row in range(10):
        label = font.render(str(row + 1), False, (255, 255, 255)) # labels 1-10, no anti-aliasing, white color
        surface.blit(label, (0, row * square_size * board_scale + label_size * board_scale)) # 

    # create labels for columns A - J
    for col in range(10):
            label = font.render(chr(ord('A') + col), False, (255, 255, 255)) # labels A-J, no anti-aliasing, white color
            surface.blit(label, (col * square_size * board_scale + label_size * board_scale, 0))

# loop to run game
running = True
board = Minesweeper()   #creates Minesweeper object
# nearly identical for loop to the one under while running
"""

I don't think this section does anything since it's only called once,
presumably at the first frame or the like.

for event in pygame.event.get():      
    # ends program if user clicks X
    if event.type == pygame.QUIT:
        running = False
    # separate left click check for initial board creation    
    if event.type == pygame.MOUSEBUTTONDOWN:
        col, row = pygame.mouse.get_pos()

        if event.button == 1:
            print(f"left click : {row}, {col}")
            if not board.setUp:
                board.createBoard(row, col) # constructs board object according to clicked space
            board.dig(row, col)
"""
            
while running:
    # checks for events such as clicks
    for event in pygame.event.get():
        # ends program if user clicks X
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # get mouse position
            pos = pygame.mouse.get_pos()
            # find board square that was clicked
            # Subtract one from each because of zero-based indexing on arrays
            col = (pos[0] // (square_size * board_scale)) - 1
            row = (pos[1] // (square_size * board_scale)) - 1
            if event.button == 1: # left click
                print(f"left click : {row}, {col}")
                # Check that position is in range; if not, continue to next iteration of loop.
                if not (0 <= col <= 9 and 0 <= row <= 9):
                    continue
                if not board.setUp:
                    # constructs board object according to clicked space
                    board.createBoard(row, col)
                # TODO (Optional): Add functionality for chords.
                board.dig(row, col)
            if event.button == 3: # right click
                print(f"right click : {row}, {col}")
                # Check that position is in range; if not, continue to next iteration of loop.
                if not (0 <= col <= 9 and 0 <= row <= 9):
                    continue
                board.flag(row, col)
        
    # display and update board
    showBoard(screen)
    pygame.display.flip()