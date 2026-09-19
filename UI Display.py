# pip install pygame-ce --pre
# required for use

# prologue
# external sources: https://www.pygame.org/docs/
# author: Emilia Davis and eliza m 

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

# displays board
def showBoard(surface):
    for row in range(10):
        for col in range(10):
            # draw sprite onto surface at given position
            #print(row, col)
            tile = board.display(row, col)
            surface.blit(sprites[tile + 3], (col * square_size * board_scale + label_size * board_scale, row * square_size * board_scale + label_size * board_scale))
                    
    for row in range(10):
        label = font.render(str(row + 1), False, (255, 255, 255)) # labels 1-10, no anti-aliasing, white color
        surface.blit(label, (0, row * square_size * board_scale + label_size * board_scale)) # 

    # create labels for columns A - J
    for col in range(10):
        label = font.render(chr(ord('A') + col), False, (255, 255, 255)) # labels A-J, no anti-aliasing, white color
        surface.blit(label, (col * square_size * board_scale + label_size * board_scale, 0)) 

running = True
menu_running = True
mines = ""
is_valid = True
while menu_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            is_valid = True
            if event.key == pygame.K_RETURN:
                try:
                    m = int(mines)
                    if 10 <= m <= 20:
                        menu_running = False
                    else:
                        raise ValueError
                except ValueError:
                    is_valid = False
            elif event.key == pygame.K_BACKSPACE:
                if mines: #checks if string is empty
                    mines = mines[:-1]
            elif event.unicode.isdigit():
                mines += event.unicode

    screen.fill((0, 0, 0))
    if is_valid:
        text = font.render("Enter Number of Mines (10-20): " + mines, False, (255, 255, 255))
    else:
        text = font.render("Enter Number of Mines (10-20): " + mines + "\nEnter a Valid Value", False, (255, 255, 255))
    screen.blit(text, ((board_size + label_size) * board_scale // 2 - text.get_width() // 2, (board_size + label_size) * board_scale // 2 - text.get_height() // 2))
    pygame.display.flip()


# loop to run game
board = Minesweeper(m)   #creates Minesweeper object
# nearly identical for loop to the one under while running
for event in pygame.event.get():      
    # ends program if user clicks X
    if event.type == pygame.QUIT:
        running = False
    # separate left click check for initial board creation    
    if event.type == pygame.MOUSEBUTTONDOWN:
        col, row = pygame.mouse.get_pos() 

        if event.button == 1:
            print(f"left click : {row}, {col}")
            board.createBoard(row, col) # constructs board object according to clicked space

win = False
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
            col = (pos[0] - label_size * board_scale) // (square_size * board_scale) #adjustments for pixels 
            row = (pos[1] - label_size * board_scale) // (square_size * board_scale) #adjustments for pixels 
            #col = pos[0] // (square_size * board_scale)
            #row = pos[1] // (square_size * board_scale)
            if event.button == 1: # left click
                if board.is_constructed == False:
                    board.createBoard(row,col)
                #eliza m added this section
                # Ryan G. modified this.
                match board.dig(row, col):
                    case 0:
                        running=False #HAHA LOZER
                    case 2:
                        if board.chord(row, col) == 0:
                            running = False
                    
                if board.status()==True:
                    win = True
                    running=False #won game!!! 
                #elif board.dig(row,col)==2: 
                #    pass
                #elif board.dig(row,col)==1: 
                    #
                #print(f"left click : {row}, {col}") 
            if event.button == 3: # right click
                board.flag(row, col) #eliza m added this line
                #print(f"right click : {row}, {col}") 
        
    # display and update board
    showBoard(screen)
    pygame.display.flip()

running = True
while running: # loop to run end screen
    for event in pygame.event.get(): # i copied this from above :3
        # ends program if user clicks X
        if event.type == pygame.QUIT:
            running = False
    # display end screen
    screen.fill((0, 0, 0)) # fill screen with black
    if win:
        text = font.render("You win. :)", False, (255, 255, 255)) # show win text
    else:
        text = font.render("You lose. :(", False, (255, 255, 255)) # show lose text
    screen.blit(text, ((board_size + label_size) * board_scale // 2 - text.get_width() // 2, (board_size + label_size) * board_scale // 2 - text.get_height() // 2)) # center text
    pygame.display.flip() # update display
    