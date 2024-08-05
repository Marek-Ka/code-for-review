# Przygotuj dekorator, który będzie wycinał listę według podanych przez użytkownika argumentów @cut(1, 10)
# <- powinien wyciąć [1:10] z podanej listy

def cut(a, b):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            del result[a:b]

            return result

        return inner_wrapper

    return wrapper


def test_cut():
    @cut(1, 10)
    def show_list():
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    result = show_list()

    assert result == [1, 11, 12, 13]
