people = [
    'zofia nowak',
    'kryStyna kowalska',
    'michał lewandowski'
]


def title_names(names: list):
    return list(map(lambda x: x.title(), names))


def get_index(string):
    return string.index(' ')


def sort_names(names: list, title_names, get_index):
    return list(sorted(title_names(names), key=lambda x: x[get_index(x) + 1]))


''' Testy '''


def test_title_names():
    assert title_names(['adam kowalski']) == ['Adam Kowalski']


def test_get_index():
    assert get_index('marek nowak') == 5


def test_sort_names():
    assert sort_names(['ma ka', 'as ds'], title_names, get_index) == ['As Ds', 'Ma Ka']


''' Koniec testów '''

sort_people = sort_names(people, title_names, get_index)
print(sort_people)
