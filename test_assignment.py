import pytest
from assignment import check_number, rectangle_area, is_divisible_by_5, sum_is_even_or_odd, divisible_by_sum_of_digits

@pytest.mark.parametrize("length, width, expected", [
    (5, 3, 15),
    (10, 2, 20),
    (7, 7, 49),
    (1, 9, 9),
    (0, 5, 0)
])
def test1(length, width, expected):
    assert rectangle_area(length, width) == expected


@pytest.mark.parametrize("num, expected", [
    (5, "Positive"),
    (-7, "Negative"),
    (0, "Neither"),
    (123, "Positive"),
    (-1, "Negative")
])
def test2(num, expected):
    assert check_number(num) == expected

@pytest.mark.parametrize("num, expected", [
    (25, True),
    (12, False),
    (0, True),
    (55, True),
    (7, False)
])
def test3(num, expected):
    assert is_divisible_by_5(num) == expected


@pytest.mark.parametrize("a, b, c, d, expected", [
    (1, 2, 3, 4, "Even"), 
    (1, 3, 4, 5, "Odd"),  
    (2, 2, 2, 2, "Even"),  
    (0, 1, 7, 3, "Odd"),  
    (9, 9, 9, 9, "Even")   
])
def test4(a, b, c, d, expected):
    assert sum_is_even_or_odd(a, b, c, d) == expected


@pytest.mark.parametrize("num, expected", [
    (121, False),    # 1+2+1=4 → 121%4=1 → False
    (456, False),    # 4+5+6=15 → 456%15=6 → False
    (132, True),     # 1+3+2=6 → 132%6=0 → True
    (111, True),     # 1+1+1=3 → 111%3=0 → True
    (123, False),    # 1+2+3=6 → 123%6=3 → False
    (222, True)      # 2+2+2=6 → 222%6=0 → True
])
def test5(num, expected):
    assert divisible_by_sum_of_digits(num) == expected
