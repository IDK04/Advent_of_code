inputs = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        inputs.append(line.strip())
gamma = str()
epsilon = str()

for digit_index in range(len(inputs[0])):
    all_digits = [line[digit_index] for line in inputs]
    gamma += '1' if all_digits.count('1') > all_digits.count('0') else '0'
    epsilon += '0' if all_digits.count('1') > all_digits.count('0') else '1'

print(int(gamma,2)*int(epsilon,2))