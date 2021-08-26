n = int(open('input.txt').read())

s = bin(n)[2:]
max = 0
for i in range(len(s)):
    n = int(s, base=2)
    if n > max:
        max = n
    s = s[1:] + s[0]

print(max, file=open('output.txt', 'w'))
