c = float(open('input.txt').read())


f = lambda x: x ** 2 + x ** (0.5)


low = 1
high = 1e10

while True:
    if low > high - 0.0000001: break
    mid = (low + high) / 2
    if f(mid) < c:
        low = mid
    else:
        high = mid

print(mid, file=open('output.txt', 'w'))