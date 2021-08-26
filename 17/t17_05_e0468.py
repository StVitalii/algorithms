array = list(map(int, open('input.txt').read().split()))

if array[1] > array[0]:
    min = array[0]
    max = float('inf')
else:
    max = array[0]
    min = -float('inf')
for i, el in enumerate(array[1:]):
    if min < el < max:
        if el > array[i]:
            min = array[i]
        else:
            max = array[i]
    else:
        s = 'NO'
        break
else:
    s = 'YES'

open('output.txt', 'w').write(s)