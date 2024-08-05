# Czas 22:34

def rounding_to_two(function):
    def wrapper(*args, **kwargs):
        return round(function(*args, **kwargs), 2)

    return wrapper


def test_rounding_to_two():
    @rounding_to_two
    def function(value):
        return value

    assert function(1.1234) == 1.12
    assert function(1.50000) == 1.5  # wbudowana f-cja round obcina zera, czyli nie będzie tutaj 1.50, a tylko 1.5


