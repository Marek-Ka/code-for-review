with open("file.txt") as f:
    set_ips = set()
    duplicate_counter = {}

    for line in f:
        if line.strip() not in set_ips:
            set_ips.add(line.strip())
            duplicate_counter[line.strip()] = 0

        duplicate_counter[line.strip()] += 1


# Tworzymy listę elementów do usunięcia: item_to_delete, ponieważ próba usunięcia z dict podczas iteracji w python3 skończy się błędem:
#  for ip, counter in duplicate_counter.items():
# RuntimeError: dictionary changed size during iteration

item_to_delete = []
counter_of_duplication = 2
for ip, counter in duplicate_counter.items():
    if counter < counter_of_duplication:
        # wcześniej tutaj chciałem użyć
        # del duplicate_counter[ip]
        # ale kończyło się to błędem: RuntimeError: dictionary changed size during iteration
        # dlatego tworzę listę kluczy do usunięcia
        item_to_delete.append(ip)

for ip in item_to_delete:
    del duplicate_counter[ip]

print(duplicate_counter)
print('===========')
print(len(set_ips), ' - ', sorted(set_ips))
