(n, m), *edges = (tuple(map(int, line.split())) for line in open('input.txt').readlines())

d = {}
for edge in edges:
    for i, v in enumerate(edge):
        add = [0, 1]
        if i: add.reverse()
        d[v] = list(map(sum, zip(d.get(v, [0, 0]), add)))

with open('output.txt', 'w') as file:
    for k, v in sorted(d.items()):
        print(*v, file=file)

