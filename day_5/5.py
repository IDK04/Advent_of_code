crates = {}
moves = []
with open('input', 'r') as file:
    add_new_crate = True
    for line in file.readlines():

        if add_new_crate:
            for i, char in enumerate(line[:-2]):
                if char != ' ' and char not in '[]n\\':
                    crate_index = (i + 3)//4
                    if crate_index not in crates:
                        crates[crate_index] = char
                    else:
                        crates[crate_index] = char + crates[crate_index]
                try:
                    int(''.join(line.split()).strip())
                except:
                    pass
                else:
                    break
        
        else:
            this_line = line.split()
            # Move n boxes from column x to column y
            moves.append((int(this_line[1]), int(this_line[3]), int(this_line[5])))

        if line.strip() == '':
            add_new_crate = False

def move_crate_p1(crates, moves):
    for move in moves:
        number_of_boxes, first_box, second_box = move
        
        crates[second_box] += crates[first_box][-number_of_boxes:][::-1]
        crates[first_box] = crates[first_box][:-number_of_boxes]
    
    return crates

def move_crate_p2(crates, moves):
    for move in moves:
        number_of_boxes, first_box, second_box = move
        
        crates[second_box] += crates[first_box][-number_of_boxes:]
        crates[first_box] = crates[first_box][:-number_of_boxes]
    
    return crates

def get_top_crates(crates):
    top_crates = ''
    for crate_n, crate in sorted(list(crates.items())):
        top_crates += crate[-1]
    return top_crates

print(get_top_crates(move_crate_p2(crates, moves)))
