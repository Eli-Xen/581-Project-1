# pip install pygame-ce --pre
# required for use

# prologue
# external sources: https://www.pygame.org/docs/
# author: Emilia Davis

import pygame

pygame.init()

board_pixels = 160 * 4
squares = board_pixels // 10

# load screen with board_pixels x board_pixels dimensions
screen = pygame.display.set_mode((board_pixels, board_pixels))

# load sprite sheet and create list of sprites
surface = pygame.image.load("SpriteSheet.png").convert()
sprites = []
# for every sprite in the sheet
for i in range(12):
    # find the area where the sprite sits
    sprite = surface.subsurface((i * 16, 0, 16, 16))
    # scale the sprite to fit the board
    sprite = pygame.transform.scale(sprite, (squares, squares))
    # add the sprite to the list of sprites
    sprites.append(sprite)

def showBoard(surface):
    for row in range(10):
        for col in range(10):
            surface.blit(sprites[0], (col * squares, row * squares))

# loop to run game
running = True
while running:
    # checks for events such as clicks
    for event in pygame.event.get():
        # ends program if user clicks X
        if event.type == pygame.QUIT:
            running = False
    # display and update board
    showBoard(screen)
    pygame.display.flip()