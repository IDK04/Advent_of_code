commands = []
with open('input.txt') as file:
    for line in file.readlines():
        line = line.split()
        commands.append({'operation': line[0], 'value': line[1]})

hor = 0
depth = 0

for command in commands:
    hor += int(command['value']) if command['operation'] == 'forward' else 0
    if command['operation'] == 'down':
        depth += int(command['value'])
    if command['operation'] == 'up':
        depth -= int(command['value'])

print(hor * depth)