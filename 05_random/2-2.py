system_number = input('Na jaki system chcesz przekonwertować liczbę [binarny - 01 / dziesiętny - 10]: ')
number_to_change = input('Podaj liczbę do zmiany: ')

if system_number == '01':
    binary_str = ''
    number = int(number_to_change)
    while number >= 2:
        binary_str += str(number % 2)
        number = number // 2

    print(f'Podana przez Ciebie liczba {number_to_change} w systemie binarnym będzie wygladać '
          f'następująco: {binary_str}')
elif system_number == '10':
    index = len(number_to_change) - 1
    decimal_num = 0
    for char in number_to_change:
        decimal_num += int(char) * pow(2, index)
        index -= 1

    print(f'Podana przez Ciebie liczba {number_to_change} w systemie dziesiętnym będzie wygladać '
          f'następująco: {decimal_num}')
else:
    print('Podaj prawidłowy kod konwersji: 01 lub 10')
