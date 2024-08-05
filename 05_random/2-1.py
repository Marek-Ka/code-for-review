word = input('Podaj jakiś wyraz, to policzymy ilość wystąpień każdego znaku: ')

word_lower = word.lower().replace(' ', '')
word_list = list(word_lower)

char_counter = {}

for char in word_list:
    if char not in char_counter:
        count = word_list.count(char)
        char_counter[char] = count
        # print(f'Litera {char} występuje w podanym zwrocie {count} razy')
# print(char_counter)
char_counter_sorted_dsc = dict(reversed(sorted((value, key) for (key, value) in char_counter.items())))

print(char_counter_sorted_dsc)
