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
def update_board(board, coordinates):
    for y, x in coordinates:
      board[y][x] = 's'
    for row in board:
        for element in row:
            print(element, end = ' ')
        print('\n')
    return board

#Test the functions
board = create_board()
board = update_board(board, [(3,0)])
print('**********')
board = update_board(board, [(3,1)])

#Step 2. Write a movement function that gets the coordinates as a list and the direction keyword ('n','s','e','w') and adds to that list, 
#The last point “moved” - will be added in that direction. 

""" Modify the existing list by appending a new coordinate in the specified direction."""
def change_board(board, direction):
    
    y, x = board[-1]
    
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

    board.append((y,x))

#Test the change_board function
board = [(0,0)]
change_board(board,'e')
change_board(board,'e')
change_board(board,'n')
print(board)

#Step 3. Start with the initial list of [(0,0),(0,1),(0,2)] coordinates. Write a while loop, ask the user for the movement direction,  
# until the user stops it by writing ‘end’ and then draws the list as a map (as in step 1). 
# This makes the snake move and grow (combination of tasks 1 and 2)

def user_movement():
    snake = [(0, 0), (0, 1), (0, 2)]
    size = 10
    
    while True:
        """Create and update the board with the current snake position"""
        board = create_board(size)
        board = update_board(board, snake)
        
        user_move = input("Enter a direction (n, s, e, w) or 'end' to finish: ")
        if user_move == 'end':
            break
        
        if not change_board(snake, user_move):
            print("Invalid move! Try again.")
    
    print("User movement:", snake)

# Check the user_movement by calling the function
user_movement()

#Step 4. Change the movement function (from step 2) so that the resulting list will have the same length as the initial one (snake does not grow,
# it only moves in a direction). 
# This means the first positions are “lost” when the new ones are added in order to keep the list same lengths as in the beginning
#Step 5. Update the movement function to prevent: 
# ● moving out of the map, ● move to a point that is already in the list. 
# If that happens, repeat user input.

def change_board(board, direction):
    y, x = board[-1]
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

    if (y, x) not in board:
      board.append((y,x))
      #board[:] = board[1:]
      board.pop(0)

#Test the change_board function
board = [(0,0),(0,1)]
change_board(board,'e')
change_board(board,'e')
change_board(board,'e')
change_board(board,'e')
change_board(board,'w')

print(board)