import os
import fileinput

file_directory = os.path.dirname(os.path.abspath(__file__))
file_path_original = os.path.join(file_directory, 'original_set')
file_path_to_mark = os.path.join(file_directory, 'to_mark')

# przygotowanie listy z proxy do oznaczenia
mark_to_change = open(file_path_to_mark)
mark_list = []
for mark in mark_to_change:
    # dodanie proxy do listy z usuniętymi białymi znakami
    mark_list.append(mark.strip())

# zapisywanie do pliku w trakcie jego otwarcia - print wprowadza dane do linii pliku
# dodana opcja zapisu oryginalenego pliku
with fileinput.FileInput(file_path_original, inplace=True, backup='.bak') as file:
    for line in file:
        # rozbicie po tabulacji linii z pliku oryginalnego, żeby wyodrębnić proxy
        proxy = line.split(sep='\t')
        # sprawdzenie czy wyodrębnione proxy znajduje się w liście do oznaczenia
        if (proxy[0]) in mark_list:
            print(line.replace('GR1', 'GR2'), end='')
        else:
            print(line, end='')

mark_to_change.close()
