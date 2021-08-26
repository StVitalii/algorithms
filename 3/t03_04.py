import math


f = lambda x: math.sin(x) - x / 3


c = 0


low = 1.6
high = 3

mid = (low + high) / 2

while mid not in (low, high):
    if f(mid) > c:
        low = mid
    else:
        high = mid
    mid = (low + high) / 2

print(low)
# 2.278862660075828