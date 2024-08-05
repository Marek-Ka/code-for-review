import os


def count_lines_in_file(filename):
    with open(filename) as f:
        print(f)
        list_file = list(f)
        list_file = list(filter(None, list_file))
        print(list_file)
    f.close()


def create_set_from_file(filename):
    with open(filename) as f:
        f_set = set()
        for line in f:
            f_set.add(line.strip())
    f.close()

    return f_set


def call_for_action(action, name='Marek'):
    choice = input(f'{name} wybierz jedną z opcji: [Pokaż linie - p / Dalej: d / Zakończ: z]: ')
    while choice not in ('p', 'd', 'z',):
        choice = input(f'{name} wybierz jedną z opcji: [Pokaż linie - p / Dalej: d / Zakończ: z]: ')
    if choice == 'p':
        for proxy in action:
            print(proxy)
        ask_for_action = input(f'{name} czy kończymy na teraz? [t/n]: ')
        if ask_for_action != 'n':
            quit()
    elif choice == 'z':
        quit()


# Wyznaczenie absolutnej ścieżki do pliku, inaczej wywołanie skryptu z innego katalogu wywala error
file_directory = os.path.dirname(os.path.abspath(__file__))
file_path_a = os.path.join(file_directory, 'a.txt')
file_path_b = os.path.join(file_directory, 'b.txt')

a_set = create_set_from_file(file_path_a)
b_set = create_set_from_file(file_path_b)

# count_lines_in_file(file_path_a)
# print(f'Linii w pliku: {lines_number}')

common_from_both = a_set & b_set
unique_from_both = a_set ^ b_set
unique_from_a = a_set - b_set
unique_from_b = b_set - a_set

print(f'Wspólne dla obu plików: {len(common_from_both)}')
call_for_action(common_from_both)
print(f'Unikalne z obu plików: {len(unique_from_both)}')
call_for_action(unique_from_both)
print(f'Unikalne z a: {len(unique_from_a)}')
call_for_action(unique_from_a)
print(f'Unikalne z b: {len(unique_from_b)}')
call_for_action(unique_from_b)
print(len(a_set))
print(len(b_set))
