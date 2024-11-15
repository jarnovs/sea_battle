field = [['▢' for j in range(7)] for i in range(7)]
ship_coordinates = [['A;0','A;0','A;0'], ['B;1', 'B;1'], ['B;2', 'B;2'], ['C;1'], ['C;2'], ['C;3'], ['C;4']]


#####
from random import randint

def gencoordinates(m, n):
    seen = set()
    x, y = randint(m, n), randint(m, n)
    while True:
        seen.add((x, y))
        yield (x, y)
        x, y = randint(m, n), randint(m, n)
        while (x, y) in seen:
            x, y = randint(m, n), randint(m, n)

coords=[]
for i in range(4):
    coords.append(next(gencoordinates(1, 7 )))
print(coords)

for i in range(3):
    for j in range(i+1,4):
        if abs(coords[i][0] - coords[j][0]) <= 1 and abs(coords[i][1] - coords[j][1]) <= 1:
            print('YES')
            print(coords[i], coords[j])
            while True:
                coords[j] = next(gencoordinates(1, 7 ))
                if abs(coords[i][0] - coords[j][0]) <= 1 and abs(coords[i][1] - coords[j][1]) <= 1:
                    continue
                else:
                    break
        else:
            pass

print(coords)
for coord in coords:
    field[coord[0]-1][coord[1]-1] = '▧'




#####
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

columns = ['0','1','2','3','4','5','6','7',]
rows = ['A','B','C','D','E','F','G']

print('|'.join(columns), sep='\n')
for i in range(7):
    print(rows[i],''.join(field[i]))
print()
input('Enter coordinates (e.g. A;4): ')






print(field)
