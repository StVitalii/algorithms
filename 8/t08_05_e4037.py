def merge_sort(array):
    length = len(array)
    if length <= 1: return
    mid = length // 2
    lefthalf = array[:mid]
    righthalf = array[mid:]

    merge_sort(lefthalf)
    merge_sort(righthalf)

    i = j = k = 0
    lefthalf_len = len(lefthalf)
    righthalf_len = len(righthalf)
    while i < lefthalf_len and j < righthalf_len:
        if lefthalf[i][0] > righthalf[j][0]:
            array[k] = righthalf[j]
            j += 1
        else:
            array[k] = lefthalf[i]
            i += 1
        k += 1
    while i < lefthalf_len:
        array[k] = lefthalf[i]
        i += 1
        k += 1
    while j < righthalf_len:
        array[k] = righthalf[j]
        j += 1
        k += 1


with open('input.txt') as file:
    n = int(file.readline())
    nums = [list(map(int, row.split())) for row in file.readlines()]


merge_sort(nums)
with open('output.txt', 'w') as file:
    for num in nums:
        print(*num, sep=' ', file=file)

