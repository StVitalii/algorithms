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
            slice = array[l - 1: r]
            slice_gcd = reduce(gcd, slice)
            slice_lcm = reduce(lambda a, b: a * b / slice_gcd, slice)
            print('wins' if slice_gcd < slice_lcm else 'draw', file=file)
        else:
            array[l - 1] = r
