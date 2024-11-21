field = [['.' for i in range(7)] for j in range(7)]
ship_coords = []

import random
coordinate = random.sample(range(7),2)
ship_coords.append(coordinate)

# Generate 4 ships 1x1
new_cord = random.sample(range(7), 2)
for i in range(3):
    while True:
        check = True
        for cord in ship_coords:
            if abs(new_cord[0] - cord[0])<=1 and abs(new_cord[1] - cord[1])<=1:
                check = False
        if check == True:
            ship_coords.append(new_cord)
            break
        else:
            new_cord = random.sample(range(7), 2)

# Generate 2 ships 2x2
new_cord = random.sample(range(7), 2)
##############

print(ship_coords)

for i in ship_coords:
    x, y = i[0], i[1]
    field[x][y] = 'X'

for i in range(7):
    print(' '.join(field[i]))
