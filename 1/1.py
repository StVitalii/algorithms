import math


# 1.8

def a(n):
    s = 0  # O(1)
    for i in range(n + 1):  # O(n)
        s += i  # O(1)
    return s  # O(1)
# O(n) * O(1) = O(n)


def b(n):
    s = 0  # O(1)
    for i in range(n + 1):  # O(n)
        s += i * i  # O(n)
    return s  # O(1)
# O(n) * O(n) = O(n ** 2)


def c(n):

    return s  # O(1)


def d(n, a):
    s = 0  # O(1)
    p = 1  # O(1)
    for i in range(n + 1):  # O(n)
        s += p  # O(n)
        p *= a  # O(n)
    return s  # O(1)


def e(n):
    p = 1  # O(1)
    for i in range(1, n + 1):  # O(n)
        p *= 1 / (1 + i)  # O(n)
    return p  # O(1)


def g(n):
    p = 1  # O(1)
    fact = 1  # O(1)
    for i in range(1, n + 1):  # O(n)
        fact *= i  # O(n)
        p *= 1 / (1 + fact)  # O(n)
    return p  # O(1)


def h(n, m):
    p = 1  # O(1)
    for i in range(1, n + 1):  # O(n)
        im = i  # O(n)
        for j in range(m):   # O(nm)
            im *= i  # O(nm)
        p *= 1 / (1 + im)  # O(n)
    return p   # O(1)


# 1.10

def a(n):
    s = 0
    for i in range(n):
        s = math.sqrt(2 + s)
    return s


def b(x, n):
    s = 0
    p = x * x
    for i in range(n):
        s += p
        p *= p
    return s + 1


def c(n):
    p = 1
    for i in range(1, n + 1):
        p *= (1 + 1 / i ** i)
    return p


def d(x, n):
    s = 0
    sin = math.sin(x)
    p = 1
    for i in range(n):
        p *= sin
        s += p
    return s + 1


print('', '====', '1.10', '====', a(3), b(3, 3), c(3), d(3, 3), sep='\n')


# 1.12

def f(n):
    '''returns the sum of first n natural numbers'''
    sum = 0  # O(1)
    for i in range(1, n + 1):  # O(n)
        sum = sum + i  # O(1)
    return sum  # O(1)
# O(n) * O(1) = O(n)


print('', '====', '1.12', '====', f(5), sep='\n')


def f(n):
    return n * (n + 1) / 2  # O(1)
# O(1)


print(f(5))
