# Korzystając z rekurencji wyświetl sumę wyrazów ciągu Fibonacciego fibonacci_sum(10) powinno zwrócić:
# 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + 34 + 55

def fibonacci_sum(num):
    fibo_list = [1, 1]
    while len(fibo_list) < num:
        fibo_list.append(fibo_list[len(fibo_list) - 2] + fibo_list[len(fibo_list) - 1])
        fibonacci_sum(num - 1)

    return fibo_list


def test_fibonacci_sum():
    assert fibonacci_sum(6) == [1, 1, 2, 3, 5, 8]


print(fibonacci_sum(10))