import os

shots = 0

# Function for clearing the window
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# Generating field and ships
field = [['▢' for j in range(7)] for i in range(7)]
ship_coordinates = [['C;4','D;4','E;4'], ['G;1', 'G;2'], ['C;6', 'D;6'], ['A;2'], ['A;5'], ['D;1'], ['G;6']]

preview = '''
   _____               ____        __  __  __        __
  / ___/___  ____ _   / __ )____ _/ /_/ /_/ /__     / /
  \__ \/ _ \/ __ `/  / __  / __ `/ __/ __/ / _ \   / / 
 ___/ /  __/ /_/ /  / /_/ / /_/ / /_/ /_/ /  __/  /_/  
/____/\___/\__,_/  /_____/\__,_/\__/\__/_/\___/  (_)   
'''

instruction = '''
▢ - empty square
▧ - sunk
▣ - hit
◆ - miss
'''

def print_field():
    columns = ['0','1','2','3','4','5','6','7',]
    rows = ['A','B','C','D','E','F','G']
    print('|'.join(columns), sep='\n')
    for i in range(7):
        print(rows[i],''.join(field[i]))

#transform coordinates (A;5) to matrix numbers (0;4)
def transform(coordinates):
    coords = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, }
    row, column = coordinates.split(';')
    return([coords[row], int(column)-1])

#marks coordinates
def hit(coordinates):
    global field
    row, column = transform(coordinates)
    field[row][column] = '▣'

def miss(coordinates):
    global field
    row, column = transform(coordinates)
    field[row][column] = '◆'

def sunk(ship):
    global field
    for coordinate in ship:
        row, column = transform(coordinate)
        field[row][column] = '▧'

def if_no_ship_left():
    global shots
    all_ships = [coordinate for ship in ship_coordinates for coordinate in ship]
    coordinates = [field[transform(coordinate)[0]][transform(coordinate)[1]] for coordinate in all_ships]

    if coordinates == ['▧']*len(all_ships):
        clear()
        print(preview)
        print_field()
        print('Congratulation! You have found all ships and made:', shots, 'shots.')
    else:
        game()

def if_ship_destroyed(coordinates):
    global ship_coordinates
    ship = [ship for ship in ship_coordinates if coordinates in ship][0]
    ship_cells = [field[transform(coordinate)[0]][transform(coordinate)[1]] for coordinate in ship]
    if ship_cells == ['▣']*len(ship):
        sunk(ship)
        if_no_ship_left()
    else:
        game()

def ship_in_coordinates(coordinates):
    global shots
    if any(coordinates in ship for ship in ship_coordinates):
        hit(coordinates)
        shots+=1
        if_ship_destroyed(coordinates)
    else:
        miss(coordinates)
        shots+=1
        game()

def cell_availabe(coordinates):
    row, column = coordinates.split(';')
    if row in 'ABCDEFG' and column in '1234567':
        row, column = transform(coordinates)
        if field[row][column] == '▢':
            ship_in_coordinates(coordinates)
        else:
            print('Cell have been already shot. Please enter coordinates again')
            input('Press to continue')
            game()
    else:
        print('Cell out of field. Please enter coordinates again')
        input('Press to continue')
        game()

def game():
    clear()
    print(preview)
    print_field()
    coordinates = input('Enter coordinates as (A;1): ')
    cell_availabe(coordinates)

clear()
print(preview)
name=input('Welcome to the Sea Battle! Please enter your name: ')
print(instruction)
input('Press any key after reading instruction above')
game()

choice = 'Do you want to start a new game? (Yes/No): '
if choice == 'Yes':
    game()
else:
    pass
