# Czas: 22:43
import math
numbers = [16, 36, 25, 49]


def pierwiastek(nums: list):
    return list(
        filter(
            lambda n: n % 2 == 0,
            map(math.sqrt, nums)
        )
    )


def test_pierwiastek():
    assert pierwiastek([9, 4, 25]) == [2]


print(pierwiastek(numbers))
