f = lambda x: x ** 3 + 4 * x ** 2 + x - 6


c = 0


low = 0
high = 2

mid = (low + high) / 2

while mid not in (low, high):
    if f(mid) < c:
        low = mid
    else:
        high = mid
    mid = (low + high) / 2

print(low)
# 0.9999999999999999