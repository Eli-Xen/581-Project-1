from minesweeper import Minesweeper

board = Minesweeper()
s_cell = input("Enter cell: ") #cell entered as [r][c] (origin is "00")
board.createBoard(int(s_cell[0]), int(s_cell[1]))

#function to handle displaying board
#similar functionality should be implemented in showBoard (UI Display.py)
def show():
    for i in range(10):
        line_str = []
        for j in range(10):
            out_ch = board.display(i, j)
            if out_ch == -3:
                line_str.append(" ")
            elif out_ch == -2:
                line_str.append("0")
            elif out_ch == -1:
                line_str.append("X")
            elif out_ch == 0:
                line_str.append("?")
            else:
                line_str.append(str(out_ch))
        print(line_str)

show()

#simple loop to run game
while(True): 
    cell = input("Input: ") #input as d[r][c] for dig and f[r][c] for flag
    try:
        if cell[0] == 'd':
            if board.dig(int(cell[1]), int(cell[2])) == 0:
                show()
                print("lose")
                break
            if board.status() == True:
                show()
                print("win")
                break
        elif cell[0] == 'f':
            board.flag(int(cell[1]), int(cell[2]))
    except:
        print("bad")

    show()

del board