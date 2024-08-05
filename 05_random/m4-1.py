# Przygotuj funkcję, która będzie odbierała argumenty w postaci:
# group_them(wall='red', tomato='red', light='yellow', lemon='yellow', grass='green')
# W odpowiedzi funkcja powinna wyświetlić (w osobnych wierszach):
# Wall is red \n Tomato is red \n Light is yellow itd.

def print_kwargs(**kwargs):
    return {print(f'{kwarg.title()} is {color}') for kwarg, color in kwargs.items()}


# capsys zbiera to co jest wyświetlane printem
def test_print_kwargs(capsys):
    print_kwargs(wall='red', tomato='red', light='yellow', lemon='yellow', grass='green')
    out, err = capsys.readouterr()

    assert out == 'Wall is red\nTomato is red\nLight is yellow\nLemon is yellow\nGrass is green\n'

