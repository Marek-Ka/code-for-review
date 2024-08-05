from math import floor

min_int = int(input('Podaj liczbę minimalną: '))
max_int = int(input('Podaj liczbę maksymalną: '))
prime_numbers = []
not_prime = None

if min_int == 1:
    min_int = 2
for num in range(min_int, max_int + 1):
    if num in [3, 5]:
        prime_numbers.append(num)
    for i in range(2, num // 2):
        if (num % i) == 0:
            not_prime = None
            break
        not_prime = True
    if not_prime is not None:
        prime_numbers.append(num)

print('Liczby pierwsze z podanego zakresu:')
for prime in prime_numbers:
    print(prime)

#### Rozwiązanie Kacpra:

for number in range(min_int, max_int + 1):
    is_prime = True
    # Podzielniki dla liczb pierwszych możemy sprawdzać do pierwiastka z liczby podniesione w górę + 1
    for divider in range(2, floor(number ** 0.5) + 1):
        if number % divider == 0:
            is_prime = False
            break
    if is_prime:
        print(number)
