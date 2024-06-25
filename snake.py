#Step 1. Write the function that gets the list of coordinates as an argument (pairs of numbers <10). 
#First number in the pair is rows (x coordinate), second number in the pair is columns (y coordinate)

""""This function allows to initialize the table of dots"""
def create_table(size=10): #10x10 grid
    table = []
    for x in range(size):
        row = []
        for y in range(size):
            row.append('.')
        table.append(row)
    return table

table = create_table()

""""This function gets a list of coordinates and outputs them as a 'X' on the map of dots"""
table[3][0] = 'x'

for row in table:
    for element in row:
        print(element, end = ' ')
    print('\n') 

#Step 2. Write a movement function that gets the coordinates as a list and the direction keyword ('n','s','e','w') and adds to that list, 
#The last point “moved” - will be added in that direction.

""" Modify the existing list by appending a new coordinate in the specified direction """
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