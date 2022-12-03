rucksacks = []
'''
1st part
with open('input', 'r') as file:
    for line in file.readlines():
        rucksacks.append(line)
'''

with open('input', 'r') as file:
    counter = 0
    new_group = []
    for line in file.readlines():
        new_group.append(line.strip())
        counter += 1
        if counter == 3:
            rucksacks.append(new_group)
            counter = 0
            new_group = []

def get_group_shared_item(group):
    for d in group[0]:
        if d in group[1] and d in group[2]:
            return d

def get_shared_item(rucksack):
    first_half = rucksack[:len(rucksack)//2]
    second_half = rucksack[len(rucksack)//2:]
    for d in first_half:
        if d in second_half:
            return d

def get_priority(digit):
    if digit.islower():
        return ord(digit)-ord('a')+1
    else:
        return 27 + (ord(digit)-ord('A'))

priorities = []
'''
1st part
for rucksack in rucksacks:
    item = get_shared_item(rucksack)
    priorities.append(get_priority(item))'''

for group in rucksacks:
    priorities.append(get_priority(get_group_shared_item(group)))

print(sum(priorities))