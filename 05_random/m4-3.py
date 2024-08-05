# Korzystając z rekurencji znajdź największy wspólny dzielnik metodą Euklidesa.

def count_tbcd(a, b):
    if a % b == 0:
        return b

    return count_tbcd(b, a % b)


def test_count_tbcd():
    assert count_tbcd(282, 78) == 6

