# Czas: 1:00:00

def play_game(player_choice: str, computer_choice: str) -> int:
    if player_choice == computer_choice:
        return 0
    player_wins = [('kamień', 'nożyce'), ('nożyce', 'papier'), ('papier', 'kamień')]
    for player in player_wins:
        if (player_choice, computer_choice) == player:
            return 1
        else:
            return 2


def test_player_win():
    assert play_game('kamień', 'nożyce') == 1


def test_computer_win():
    assert play_game('kamień', 'papier') == 2


def test_draw():
    assert play_game('kamień', 'kamień') == 0

