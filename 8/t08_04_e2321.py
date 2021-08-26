def qsort(array, a, b):
    if a >= b: return
    pivot = array[(a + b) // 2]
    l = a
    r = b
    while True:
        while array[l] < pivot:
            l += 1
        while array[r] > pivot:
            r -= 1
        
        if l >= r: break
        array[l], array[r] = array[r], array[l]
        l += 1
        r -= 1
    qsort(array, a, r)
    qsort(array, r + 1, b)

n, *array = map(int, open('input.txt').read().split())

qsort(array, 0, len(array) - 1)
print(*array, file=open('output.txt', 'w'))