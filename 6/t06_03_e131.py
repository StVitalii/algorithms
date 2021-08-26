def get_letter_count(word: str) -> dict:
    return {letter: word.count(letter) for letter in word}


word, n, *dictionary = open('input.txt').read().split()

word_set = set(word)
word_dict = get_letter_count(word)

s = 0
for word in dictionary:
    if set(word).issubset(word_set):
        for letter, count in get_letter_count(word).items():
            if count > word_dict[letter]: break
        else: s += 1


open('output.txt', 'w').write(str(s))

