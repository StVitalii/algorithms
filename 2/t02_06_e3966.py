n1, s1, n2, s2 = open('input.txt').readlines()
s1, s2 = (list(map(int, s.split())) for s in (s1, s2))
n1 = int(n1) - 1

for i, k in enumerate(s2):
    low = 0
    high = n1
    while low <= high:
        mid = (low + high) // 2
        guess = s1[mid]
        if guess == k:
            s2[i] = 'YES'
            break
        elif guess < k:
            low = mid + 1
        else:
            high = mid - 1
    else:
        s2[i] = 'NO'

open('output.txt', 'w').write('\n'.join(s2))
