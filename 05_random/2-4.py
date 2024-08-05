pesel = input('Podaj numer PESEL: ')

multipliers = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
sum = 0

for i in range(len(pesel)):
    sum += int(pesel[i]) * multipliers[i]

sum_str = str(sum)
if int(sum_str[(len(sum_str) - 1)]) != 0:
    print('Podałeś niepoprawny PESEL')
else:
    print('Twój nr PESEL został wprowadzony prawidłowo!!')
