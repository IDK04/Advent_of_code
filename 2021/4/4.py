solutions = [46,12,57,37,14,78,31,71,87,52,64,97,10,35,54,36,27,84,80,94,99,22,0,11,30,44,86,59,66,7,90,21,51,53,92,8,76,41,39,77,42,88,29,24,60,17,68,13,79,67,50,82,25,61,20,16,6,3,81,19,85,9,28,56,75,96,2,26,1,62,33,63,32,73,18,48,43,65,98,5,91,69,47,4,38,23,49,34,55,83,93,45,72,95,40,15,58,74,70,89]
boards = []

with open('input.txt', 'r') as file:
    new_board = []
    for line in file.readlines():
        if line.strip() != '':
            new_board.append(list(int(n) for n in line.split()))
        else:
            boards.append(new_board)
            new_board = []

def ganhou(board):
    for l, line in enumerate(board):
        if all(type(value)==str for value in line):
            return True
        coluna = []
        for c in range(len(board[0])):
            coluna.append(board[c][l])
        if all(type(c)==str for c in coluna):
            return True
    return False

end = False

for solution in solutions:
    for b, board in enumerate(boards):   
        for l, line in enumerate(board):
            for v, value in enumerate(line):
                if value == solution:
                    last_number = boards[b][l][v]
                    boards[b][l][v] = 'X'
        if ganhou(board):
            numbers = [[x for x in board[i] if type(x)==int] for i in range(len(board))]
            full_sum = 0
            for line in numbers:
                full_sum += sum(line)
            print(full_sum * last_number)
            end = True
            break
    if end:
        break
