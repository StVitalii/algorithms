with open('input.txt') as file:
    n = int(file.readline())
    matrix = tuple(zip(*([map(int, file.read().split())] * n)))

print(sum(not bool(sum(row) - 1) for row in matrix), file=open('output.txt', 'w'))
