words = input('Podaj słowa rozdzielone przecinkiem: ')

words_list = words.split(',')
word1_sorted = sorted(words_list[0])
word2_sorted = sorted(words_list[1])

if words_list[0] == words_list[1][::-1]:
    print('Mamy palindromy')
elif word1_sorted == word2_sorted:
    print('Mamy anagram')
else:
    print('Słowa są różne')

