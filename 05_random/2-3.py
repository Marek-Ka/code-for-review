expression = input('Podaj wyrażenie do obróbki: ')
conversion = int(input('Chcesz zakodować [1], czy odkodować [2]? '))
shift = 3
encoded_expression = ''
decoded_expression = ''

if conversion == 1:
    for char in expression:
        if char.isalpha():
            if char.isupper():
                # ustalam indeks pozycji z przedziału 0-25
                char_index = ord(char) - ord('A')
                # wyznaczam indeks pozycji z użciem klucza
                en_char_index = (char_index + shift) % 26

                # wyznaczam indeks pozycji unicode
                en_char_unicode = en_char_index + ord('A')

                # dodajemy zakodowany znak do ciągu
                encoded_expression += chr(en_char_unicode)
            else:
                en_char_unicode = ((ord(char) - ord('a')) + shift) % 26 + ord('a')

                encoded_expression += chr(en_char_unicode)
        else:
            encoded_expression += char
    print(f'Niezakodowane wyrażenie: "{expression}" => zakodowane wyrażenie: "{encoded_expression}"')
elif conversion == 2:
    for char in expression:
        if char.isalpha():
            if char.isupper():
                de_char_unicode = ((ord(char) - ord('A')) - shift) % 26 + ord('A')

                decoded_expression += chr(de_char_unicode)
            else:
                de_char_unicode = ((ord(char) - ord('a')) - shift) % 26 + ord('a')

                decoded_expression += chr(de_char_unicode)
        else:
            decoded_expression += char
    print(f'Zakodowane wyrażenie: "{expression}" => odkodowane wyrażenie: "{decoded_expression}"')
else:
    print('Wybierz opcje pomiędzy 1 a 2')
