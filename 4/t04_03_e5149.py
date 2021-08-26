n, k, *coords = map(int, open('input.txt').read().split())


def valid(val):
    stall = 1
    l = 0
    for i in range(1, n):
        l += coords[i] - coords[i - 1]
        if l >= val:
            l = 0
            stall += 1
    return stall >= k


l, r = 0, 1e9

while l <= r:
    mid = (l + r) // 2
    if valid(mid): l = mid + 1
    else: r = mid - 1


print(int(l - 1), file=open('output.txt', 'w'))