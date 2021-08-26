requests = open('input.txt').readlines()
requests = [requests[i + 1:i + 3] for i in range(0, len(requests), 3)]

for i, request in enumerate(requests):
    request = [sorted(map(int, l.split())) for l in request]
    requests[i] = str(len(list(filter(lambda height: (
        request[1][0] - 1 < height < request[1][1] + 1), request[0]))))

open('output.txt', 'w').write('\n'.join(requests))
