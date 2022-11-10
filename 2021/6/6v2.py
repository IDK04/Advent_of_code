all_fish = [1,4,3,3,1,3,1,1,1,2,1,1,1,4,4,1,5,5,3,1,3,5,2,1,5,2,4,1,4,5,4,1,5,1,5,5,1,1,1,4,1,5,1,1,1,1,1,4,1,2,5,1,4,1,2,1,1,5,1,1,1,1,4,1,5,1,1,2,1,4,5,1,2,1,2,2,1,1,1,1,1,5,5,3,1,1,1,1,1,4,2,4,1,2,1,4,2,3,1,4,5,3,3,2,1,1,5,4,1,1,1,2,1,1,5,4,5,1,3,1,1,1,1,1,1,2,1,3,1,2,1,1,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,4,5,1,3,1,4,4,2,3,4,1,1,1,5,1,1,1,4,1,5,4,3,1,5,1,1,1,1,1,5,4,1,1,1,4,3,1,3,3,1,3,2,1,1,3,1,1,4,5,1,1,1,1,1,3,1,4,1,3,1,5,4,5,1,1,5,1,1,4,1,1,1,3,1,1,4,2,3,1,1,1,1,2,4,1,1,1,1,1,2,3,1,5,5,1,4,1,1,1,1,3,3,1,4,1,2,1,3,1,1,1,3,2,2,1,5,1,1,3,2,1,1,5,1,1,1,1,1,1,1,1,1,1,2,5,1,1,1,1,3,1,1,1,1,1,1,1,1,5,5,1]
all_fish = sorted(all_fish)

def fish_to_dict(all_fish):
    all_fish_dict = {}
    for i in range(9):
        all_fish_dict[i] = all_fish.count(i)
    return all_fish_dict

def count_debug(all_fish):
    for i in range(9):
        if i in all_fish and all_fish[i] > 0:
            print(f'{i}->{all_fish[i]}   ',end='')
        else:
            print(f'{i}->{0}   ',end='')
    print('\n')

all_fish = fish_to_dict(all_fish)
days = 256
current_day = 1
while current_day <= days:
    
    fish_to_add = all_fish[0]

    for i in range(0, 8):
        all_fish[i] = all_fish[i+1]
    
    all_fish[8] = fish_to_add
    all_fish[6] += fish_to_add

    current_day += 1

print(sum(all_fish.values()))
