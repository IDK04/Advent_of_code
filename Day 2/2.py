player_shapes = ['X', 'Y', 'Z']
elf_shapes = ['A', 'B', 'C']
rounds = []

with open('input', 'r') as file:
    for line in file.readlines():
        rounds.append(''.join(line.split()))

# Part 1
def count_round_points_1(round):
    player = player_shapes.index(round[1])
    elf = elf_shapes.index(round[0])

    if ((elf+1)%3) == player:
        return 6 + (player+1)
    elif elf == player:
        return 3 + (player+1)
    return (player+1)

# Part 2
def count_round_points_2(round):
    round_ending = round[1]
    elf = elf_shapes.index(round[0])

    if round_ending == 'X':
        # Lose case
        player = (elf-1)%3
        return (player+1)

    elif round_ending == 'Z':
        # Win case
        player = (elf+1)%3
        return (player+1) + 6

    else:
        return 3 + (elf+1)

def calculate_scores(rounds, part):
    score = 0
    for round in rounds:
        score += part(round)
    return score

print(calculate_scores(rounds, count_round_points_2))
