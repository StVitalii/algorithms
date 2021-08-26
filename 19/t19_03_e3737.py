n, *array = map(int, open('input.txt').read().split())

for i in range(n // 2):
    try:
        if array[i] > array[2 * i + 1] or array[i] > array[2 * (i + 1)]:
            s = 'NO'
            break
    except IndexError: pass
else: s = 'YES'

open('output.txt', 'w').write(s)