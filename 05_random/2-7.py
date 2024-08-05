word_1 = input('Podaj słowo nr 1: ')
word_2 = input('Podaj słowo nr 2: ')

word_1_set = set(word_1)
word_2_set = set(word_2)

print(word_1_set & word_2_set)
