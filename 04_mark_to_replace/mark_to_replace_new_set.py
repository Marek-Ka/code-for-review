import os
import fileinput
from pprint import pprint

file_directory = os.path.dirname(os.path.abspath(__file__))
file_path_original = os.path.join(file_directory, 'original_set')
file_path_to_mark = os.path.join(file_directory, 'to_mark')
file_path_to_new_set = os.path.join(file_directory, 'new_set')

# przygotowanie listy z proxy do oznaczenia
mark_to_change = open(file_path_to_mark)
mark_list = []
for mark in mark_to_change:
    # dodanie proxy do listy z usuniętymi białymi znakami
    mark_list.append(mark.strip())
# pprint(mark_list)

orig_file = open(file_path_original)
orig_list = []
for orig in orig_file:
    orig_list.append(orig.strip().split(sep='\t'))

# pprint(orig_list)

# print(len(orig_list))

new_set = open(file_path_to_new_set, 'w')

i = 0
while i < len(orig_list):
    proxy = orig_list[i][0]
    # print(proxy)
    for mark in mark_list:
        if proxy in mark:
            new_set.write(f"{mark}\n")
    i += 1

mark_to_change.close()
orig_file.close()
