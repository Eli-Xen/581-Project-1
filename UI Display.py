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
            if board.display(row, col)==-3: #eliza m added logic for what sprites to show depending on the board.display function -2,-1,0,n
                surface.blit(sprites[0], (col * square_size * board_scale + label_size * board_scale, row * square_size * board_scale + label_size * board_scale)) # TODO: right now this just draws the covered sprite for every position, needs logic to determine what sprite to use
            elif board.display(row, col)==-2: #shows flag 
                surface.blit(sprites[3], (col * square_size * board_scale + label_size * board_scale, row * square_size * board_scale + label_size * board_scale)) # TODO: right now this just draws the covered sprite for every position, needs logic to determine what sprite to use
            elif board.display(row, col)==-1: #shows mine >:) mwehehehe  
                surface.blit(sprites[2], (col * square_size * board_scale + label_size * board_scale, row * square_size * board_scale + label_size * board_scale)) # TODO: right now this just draws the covered sprite for every position, needs logic to determine what sprite to use
            elif board.display(row, col)==0: #shows cell digit=0 
                surface.blit(sprites[1], (col * square_size * board_scale + label_size * board_scale, row * square_size * board_scale + label_size * board_scale)) # TODO: right now this just draws the covered sprite for every position, needs logic to determine what sprite to use
            elif board.display(row, col)==1: #shows cell digit=1 spite 4 
                surface.blit(sprites[4], (col * square_size * board_scale + label_size * board_scale, row * square_size * board_scale + label_size * board_scale)) # TODO: right now this just draws the covered sprite for every position, needs logic to determine what sprite to use
            elif board.display(row, col)==2: #shows cell digit=2 spite 5 
                    surface.blit(sprites[5], (col * square_size * board_scale + label_size * board_scale, row * square_size * board_scale + label_size * board_scale)) # TODO: right now this just draws the covered sprite for every position, needs logic to determine what sprite to use
            elif board.display(row, col)==3: #shows cell digit=3 spite 6 
                    surface.blit(sprites[6], (col * square_size * board_scale + label_size * board_scale, row * square_size * board_scale + label_size * board_scale)) # TODO: right now this just draws the covered sprite for every position, needs logic to determine what sprite to use
            elif board.display(row, col)==4: #shows cell digit=4 spite 7 
                    surface.blit(sprites[7], (col * square_size * board_scale + label_size * board_scale, row * square_size * board_scale + label_size * board_scale)) # TODO: right now this just draws the covered sprite for every position, needs logic to determine what sprite to use
            elif board.display(row, col)==5: #shows cell digit=5 spite 8
                    surface.blit(sprites[8], (col * square_size * board_scale + label_size * board_scale, row * square_size * board_scale + label_size * board_scale)) # TODO: right now this just draws the covered sprite for every position, needs logic to determine what sprite to use
            elif board.display(row, col)==6: #shows cell digit=6 spite 9
                    surface.blit(sprites[9], (col * square_size * board_scale + label_size * board_scale, row * square_size * board_scale + label_size * board_scale)) # TODO: right now this just draws the covered sprite for every position, needs logic to determine what sprite to use
            elif board.display(row, col)==7: #shows cell digit=7 spite 10
                    surface.blit(sprites[10], (col * square_size * board_scale + label_size * board_scale, row * square_size * board_scale + label_size * board_scale)) # TODO: right now this just draws the covered sprite for every position, needs logic to determine what sprite to use
            elif board.display(row, col)==8: #shows cell digit=8 spite 11 
                    surface.blit(sprites[11], (col * square_size * board_scale + label_size * board_scale, row * square_size * board_scale + label_size * board_scale)) # TODO: right now this just draws the covered sprite for every position, needs logic to determine what sprite to use

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
for event in pygame.event.get():      
    # ends program if user clicks X
    if event.type == pygame.QUIT:
        running = False
    # separate left click check for initial board creation    
    if event.type == pygame.MOUSEBUTTONDOWN:
        col, row = pygame.mouse.get_pos() #is this by sprite or what d0es this return?? 

        if event.button == 1:
            print(f"left click : {row}, {col}")
            board.createBoard(row, col) # constructs board object according to clicked space #create board takes position bvt what does get_pos() ret? 
            
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
                if board.dig(row,col)==0: #eliza m added this section; i think this is rite? 
                    running=False #HAHA LOZER 
                elif board.status()==True: 
                    running=False #won game!!! 
                #elif board.dig(row,col)==2: 
                #    pass
                #elif board.dig(row,col)==1: 
                    #
                #print(f"left click : {row}, {col}") # TODO: add logic
            if event.button == 3: # right click
                board.flag(row, col) #eliza m added this line; i think this is rite? 
                #i th1nk i need 
                #print(f"right click : {row}, {col}") # TODO: add logic
        
    # display and update board
    showBoard(screen)
    pygame.display.flip()