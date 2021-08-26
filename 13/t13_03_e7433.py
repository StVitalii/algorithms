a, p = map(int, open('input.txt').readlines())

s = ''
while True:
    r = a % p
    a //= p
    if r > 9: r = [r]
    s = f'{r}{s}'
    if not a: break

open('output.txt', 'w').write(s)
