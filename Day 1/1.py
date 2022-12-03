food = []
with open('input.txt', 'r') as file:
    new_elve = []
    for line in file.readlines():
        try:
            new_elve.append(int(line))
        except:
            food.append(new_elve)
            new_elve = []

def max_calories(food):
    max_food = max(map(sum, food))
    food_len = len(food)-1
    while food_len >= 0:
        if max_food == sum(food[food_len]):
            food.pop(food_len)
            return (max_food, food)
        food_len -= 1

total = 0

for i in range(3):
    max_food, food = max_calories(food)
    total += max_food

print(total)