# Czas: 1:00:00
vowels = 'aeyuioąęóAEVUIOĄÓ'


def remove_evals(text: str):
    # new_text = ''
    #
    # for char in str(text):
    #     if char not in evals:
    #         new_text += char
    #
    # return new_text

    return ''.join(char for char in str(text) if char not in vowels)


def test_remove_evals():
    assert remove_evals('Ala ma kota') == 'l m kt'
    assert remove_evals('abrAkADAbra') == 'brkDbr'
    assert remove_evals('') == ''
