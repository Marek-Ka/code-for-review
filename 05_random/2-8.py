words = input('Podaj słowa rozdzielone przecinkami: ')

words_set = set()
words_list = words.split(',')

for word in words_list:
    words_set.add(word)

for word in words_set:
    print(word)

###### Rozwiązanie Kacpra:

for word in set(words.split(',')):
    print(word)
