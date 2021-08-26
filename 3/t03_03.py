f = lambda x: x ** 3 + x + 1


c = 5


low = 0
high = 10

mid = (low + high) / 2

while mid not in (low, high):
    if f(mid) < c:
        low = mid
    else:
        high = mid
    mid = (low + high) / 2

print(low)
# 1.3787967001295507