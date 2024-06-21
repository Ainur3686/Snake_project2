#Step 1. Write the function that gets the list of coordinates as an argument (pairs of numbers <10). 10x10 grid.
#First number in the pair is rows (x coordinate), second number in the pair is columns (y coordinate)

""""This function allows to initialize the table of dots"""
def create_table(size=10):
    table = []
    for x in range(size):
        row = []
        for y in range(size):
            row.append('.')
        table.append(row)
    return table

table = create_table()

table[3][0] = 'x'

for row in table:
    for element in row:
        print(element, end = ' ')
    print('\n')