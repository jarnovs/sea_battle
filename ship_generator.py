import random

ships = []

freezone = set()
for i in range(7):
    for j in range(7):
        freezone.add((i,j))

def random_direction():
    direction = random.randint(0,1)
    return direction

def transform(coordinate):
    coords = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    row, column = coordinate[0], coordinate[1]
    row, column = [coords[row], column+1]
    coordinate = row+';'+str(column)
    return coordinate

def del_from_freezone(coordinates):
    for coordinate in coordinates:
        freezone.discard(coordinate)
        x,y = coordinate[0], coordinate[1]
        freezone.discard((x+1,y))
        freezone.discard((x-1,y))
        freezone.discard((x,y+1))
        freezone.discard((x,y-1))
        freezone.discard((x+1,y+1))
        freezone.discard((x-1,y-1))
        freezone.discard((x+1,y-1))
        freezone.discard((x-1,y+1))

def big_ship():
    global freezone
    global ships
    if random_direction() == 1:
        first_cell = (random.randint(0,6), random.randint(0,4))
        second_cell = (first_cell[0], first_cell[1]+1)
        third_cell = (first_cell[0], first_cell[1]+2)
        ships.append([first_cell,second_cell,third_cell])
        del_from_freezone([first_cell,second_cell,third_cell])
    else:
        first_cell = (random.randint(0,4), random.randint(0,6))
        second_cell = (first_cell[0]+1, first_cell[1])
        third_cell = (first_cell[0]+2, first_cell[1])
        ships.append([first_cell,second_cell,third_cell])
        del_from_freezone([first_cell,second_cell,third_cell])

def medium_ship():
    global ships
    global freezone
    if random_direction() == 1:
        first_cell = random.choice(list(freezone))
        if 0<=first_cell[0]<=6 and 0<=first_cell[1]<=5:
            second_cell = (first_cell[0], first_cell[1]+1)
            if second_cell in freezone:
                ships.append([first_cell,second_cell])
                del_from_freezone([first_cell,second_cell])
            else:
                medium_ship()
                return 0
        else:
            medium_ship()
            return 0
    
    else:
        first_cell = random.choice(list(freezone))
        if 0<=first_cell[0]<=5 and 0<=first_cell[1]<=6:
            second_cell = (first_cell[0]+1, first_cell[1])
            if second_cell in freezone:
                ships.append([first_cell,second_cell])
                del_from_freezone([first_cell,second_cell])
            else:
                medium_ship()
                return 0
        else:
            medium_ship()
            return 0

def one_ship():
    global ships
    global freezone
    first_cell = random.choice(list(freezone))
    ships.append([first_cell])
    del_from_freezone([first_cell])

def last_one_ship():
    global ships
    global freezone
    if len(freezone) == 0:
        ship = []
        big_ship()
        medium_ship()
        medium_ship()
        one_ship()
        one_ship()
        one_ship()
        last_one_ship()
    else:
        first_cell = random.choice(list(freezone))
        ships.append([first_cell])
        del_from_freezone([first_cell])
        
def field_generation():
    global ships
    ships = []
    big_ship()
    medium_ship()
    medium_ship()
    one_ship()
    one_ship()
    one_ship()
    last_one_ship()

field_generation()
ship_coordinates = [[transform(coordinate) for coordinate in ship] for ship in ships]
