n, r, *coords = map(int, open('input.txt').read().split())
coords = list(zip(*([iter(coords)] * 2)))

count = sum(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (0.5) < r for i, (x1, y1) in enumerate(coords) for x2, y2 in coords[i + 1:])

print(count, file=open('output.txt', 'w'))