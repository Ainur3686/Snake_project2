#Step 1. Write the function that gets the list of coordinates as an argument (pairs of numbers <10). 
#First number in the pair is rows (x coordinate), second number in the pair is columns (y coordinate)

""""This function allows to initialize the table of dots"""
def create_board(size=10): #10x10 grid
    board = []
    for x in range(size):
        row = []
        for y in range(size):
            row.append('.')
        board.append(row)
    return board

""""This function gets a list of coordinates and outputs them as a 'X' on the map of dots"""
def update_board(board, coordinate):
    board[coordinate[0]][coordinate[1]] = 'x'
    for row in board:
        for element in row:
            print(element, end = ' ')
        print('\n')
    return board

board = create_board()
board = update_board(board, (3,0))
print('**********')
board = update_board(board, (3,1))

#Step 2. Write a movement function that gets the coordinates as a list and the direction keyword ('n','s','e','w') and adds to that list, 
#The last point “moved” - will be added in that direction. 

""" Modify the existing list by appending a new coordinate in the specified direction."""
def change_table(table, direction):
    
    y, x = table[-1]
    
    if direction == 'e' and x < 9:
      x += 1
    elif direction == 'w' and x > 0:
      x -= 1
    elif direction == 'n' and y > 0:
      y -= 1
    elif direction == 's' and y < 9:
      y += 1
    else:
       return False 

table.append((y,x))

table = [(0,0)]
change_table(table,'e')
change_table(table,'e')
change_table(table,'n')
print(table)

#Step 3. Start with the initial list of [(0,0),(0,1),(0,2)] coordinates. Write a while loop, ask the user for the movement direction,  
# until the user stops it by writing ‘end’ and then draws the list as a map (as in step 1). 
# This makes the snake move and grow (combination of tasks 1 and 2)

