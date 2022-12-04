groups = []
with open('input', 'r') as file:
    for line in file.readlines():
        line = line.strip().split(',')
        first_pair, second_pair = line[0].split('-'), line[1].split('-')
        groups.append((list(map(int, first_pair)), list(map(int, second_pair))))

def count_contained_groups(groups):
    counter = 0
    for group in groups:
        first_pair, second_pair = group
        if first_pair[0] >= second_pair[0] and first_pair[1] <= second_pair[1]:
            counter += 1
        elif second_pair[0] >= first_pair[0] and second_pair[1] <= first_pair[1]:
            counter += 1
    return counter

def count_total_overlaps(groups):
    counter = 0
    for group in groups:
        first_pair, second_pair = group
        if first_pair[0] >= second_pair[0] and first_pair[1] <= second_pair[1]:
            counter += 1
        elif second_pair[0] >= first_pair[0] and second_pair[1] <= first_pair[1]:
            counter += 1
        elif first_pair[0] <= second_pair[1] and second_pair[0] <= first_pair[1]:
            counter += 1
    return counter
