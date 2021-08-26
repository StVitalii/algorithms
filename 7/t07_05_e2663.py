with open('input.txt') as file:
    n = int(file.readline())
    arr = list(map(int, file.readline().split()))

    k = 0
    for j in range(n):
        for i in range(n - j - 1):
            if arr[i] > arr[i + 1]:
                k += 1
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    print(k, file=open('output.txt', 'w'))