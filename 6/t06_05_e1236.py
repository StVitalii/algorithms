with open('input.txt') as file:
    n = int(file.readline())
    words = dict.fromkeys(filter(None, [file.readline().strip() for _ in range(n)]), 0)
    for j, char in enumerate(file.read()):
        for word, ind in words.items():
            if char == word[ind]:
                words[word] += 1
                if words[word] == len(word): break
        else: continue
        s = 'YES '
        j = str(j + 1)
        break
    else:
        s = 'NO'
        j = ''

open('output.txt', 'w').write(s + j)

