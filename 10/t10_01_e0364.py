n, k = map(int, open('input.txt').read().split())

def permutations(elements):
    if len(elements) <= 1: yield elements
    else:
        for perm in permutations(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

letters = ''.join(chr(97 + i) for i in range(n))

open('output.txt', 'w').write(sorted(permutations(letters))[k - 1])