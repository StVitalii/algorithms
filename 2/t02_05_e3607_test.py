requests = open('input.txt').readlines()
requests = [requests[i:i + 3] for i in range(0, len(requests), 3)]

for j, request in enumerate(requests):
    height_list, (l, u) = [sorted(map(int, l.split())) for l in request[1:]]
    high0 = int(request[0]) - 1

    low = 0
    high = high0
    while low < high:
        mid = (low + high) // 2
        guess = height_list[mid]
        if guess < l:
            low = mid + 1
        else:
            high = mid - 1
    mid = (low + high) // 2
    lower = mid

    low = lower
    high = high0
    while low < high:
        mid = (low + high) // 2
        guess = height_list[mid]
        if guess > l:
            high = mid - 1
        else:
            low = mid + 1
    mid = (low + high) // 2
    upper = mid

    requests[j] = str(upper - lower + 1)

open('output.txt', 'w').write('\n'.join(requests))
