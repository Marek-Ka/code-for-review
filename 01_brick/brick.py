# Czas: 1:00:00
import random
import time
import sys

options = {
    'k': 'kamień',
    'p': 'papier',
    'n': 'nożyce',
    's': 'studnia'
}
player_wins = [
    ('kamień', 'nożyce'),
    ('nożyce', 'papier'),
    ('papier', 'studnia'),
    ('papier', 'kamień'),
    ('studnia', 'kamień'),
    ('studnia', 'nożyce')
]


def play_game(player_choice: str, computer_choice: str) -> int:
    if player_choice == computer_choice:
        return 0

    for player in player_wins:
        if (player_choice, computer_choice) == player:
            return 1

    return 2


def get_score(name):
    player_counter = 0
    computer_counter = 0
    stop_play = False
    while stop_play is False:
        if player_counter == 5:
            stop_play = True
            print(f'Brawo {name}! Zwycięstwo {player_counter} : {computer_counter}')
            continue
        if computer_counter == 5:
            stop_play = True
            print(f'Tym razem się nie udało. Komputer wygrał {computer_counter} : {player_counter}'
                  f'\nNie poddawaj się!')
            continue
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        score = play_game(player_choice, computer_choice)
        for printer in (player_choice, ' - ', computer_choice):
            sys.stdout.write(printer)
            sys.stdout.flush()
            time.sleep(2)
        if score == 0:
            print('\nRemis!')
            print(f'Wynik pozostaje bez zmian: {name}: {player_counter} - Komputer: {computer_counter}')
        elif score == 1:
            print(f'\nŚwietnie {name}! Punkt dla Ciebie!')
            player_counter += 1
            print(f'Aktualny wynik: {name}: {player_counter} - Komputer: {computer_counter}')
        elif score == 2:
            print('\nPunkt dla komputera')
            computer_counter += 1
            print(f'Aktualny wynik: {name}: {player_counter} - Komputer: {computer_counter}')


def get_player_choice():
    player_choice = input('Podaj swój wybór (pierwszą literę danego wyboru): ')
    while player_choice not in 'kpns':
        print('Wybierz jedną z liter: "kpns"')
        player_choice = input('Podaj swój wybór: ')
    for letter, choice in options.items():
        if player_choice == letter:
            player_choice = choice

    return player_choice


def get_computer_choice():
    return str(random.choice(list(options.values())))


name = input('Podaj swoje imie: ')
get_score(name)
