nums = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        nums.append(int(line))

increased = 0
for i in range(1, len(nums)):
    increased += 1 if nums[i] > nums[i-1] else 0
print(increased)