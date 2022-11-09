lines = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip().split(' -> ')
        lines.append([tuple(int(v) for v in l.split(',')) for l in line])

def lines_to_add_hor(coords):
    coords = sorted(coords, key=lambda coord: (coord[0], coord[1]))
    coord1, coord2 = coords[0], coords[1]
    return [(x,coord1[1]) for x in range(coord1[0], coord2[0]+1)]

def lines_to_add_ver(coords):
    coords = sorted(coords, key=lambda coord: (coord[0], coord[1]))
    coord1, coord2 = coords[0], coords[1]
    return [(coord1[0], y) for y in range(coord1[1], coord2[1]+1)]

def lines_to_add_dia(coords):
    coords = sorted(coords, key=lambda coord: (coord[0], coord[1]))
    coord1, coord2 = coords[0], coords[1]
    coord2_y = coord2[1]
    coord2_x = coord2[0]

    coords_to_add = [coord1]
    new_coord = coord1
    while new_coord != coord2:
        new_x = new_coord[0]
        new_y = new_coord[1]
        
        if new_x < coord2_x:
            new_x += 1
        if new_x > coord2_x:
            new_x -= 1
        if new_y < coord2_y:
            new_y += 1
        if new_y > coord2_y:
            new_y -= 1
        
        new_coord = (new_x, new_y)
        coords_to_add.append(new_coord)
    return coords_to_add

paths = []

for l in lines:
    if l[0][0] == l[1][0]:
        paths += lines_to_add_ver(l)
    elif l[0][1] == l[1][1]:
        paths += lines_to_add_hor(l)
    else:
        paths += lines_to_add_dia(l)


counts = {}

for path in paths:
    if path in counts:
        counts[path] += 1
    else:
        counts[path] = 1

counter = 0
for path in counts:
    if counts[path] >= 2:
        counter += 1
print(counter)
