with open('input.txt') as file:
    n = int(file.readline())
    words = file.read().split()


for j in range(n):
    min_idx = j
    for i, word in enumerate(words[j + 1:]):
        if word < words[min_idx]:
            min_idx = i + j + 1
    words[j], words[min_idx] = words[min_idx], words[j]

open('output.txt', 'w').write('\n'.join(words))
