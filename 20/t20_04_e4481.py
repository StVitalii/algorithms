from math import gcd
from functools import reduce


with open('input.txt') as file:
    n = int(file.readline())
    array = list(map(int, file.readline().split()))
    m = int(file.readline())
    requests = list(zip(*([map(int, file.read().split())] * 3)))

with open('output.txt', 'w') as file:
    for q, l, r in requests:
        if q == 1:
            print(reduce(gcd, array[l - 1: r]), file=file)
        else:
            array[l - 1] = r
