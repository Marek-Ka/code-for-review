#Czas 22:34
from time import time


def show_time_and_args(function):
    def wrapper(*args, **kwargs):
        start = time()
        result = function(*args, **kwargs)
        end = time()
        time_elapsed = end - start
        print(f'Cas wykonywania funkcji: {time_elapsed}')
        print(f'Przesłane w funkcji argumenty: {[arg for arg in args]}')
        print(f'Kwargs: {kwargs}')

        return result

    return wrapper


def test_show_time_and_args():
    @show_time_and_args
    def function(num=0):
        while num < 100:
            print(num)
            num += 1

        return num

    result = function(2)

    assert result == 100


@show_time_and_args
def count_to_hundred(num=0, end=100):
    while num < end:
        print(num)
        num += 1

    return num


resultito = count_to_hundred(20, 50)
print(resultito)
