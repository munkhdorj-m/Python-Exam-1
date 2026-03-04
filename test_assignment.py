import pytest
import inspect
from assignment import *


def check_contains_loop(func):
    source = inspect.getsource(func)
    return "for " in source or "while " in source


# Exercise 1
@pytest.mark.parametrize("h,m,s,expected", [
    (1, 2, 3, 3723),
    (0, 0, 0, 0),
    (0, 0, 59, 59),
    (0, 1, 0, 60),
    (2, 30, 0, 9000),
    (10, 59, 59, 39599),
])
def test1(h, m, s, expected):
    assert time_to_seconds(h, m, s) == expected


# Exercise 2
@pytest.mark.parametrize("y,m,expected", [
    (2, 7, 31),
    (0, 5, 5),
    (1, 0, 12),
    (10, 0, 120),
    (0, 0, 0),
])
def test2(y, m, expected):
    assert years_months_to_months(y, m) == expected


# Exercise 3
@pytest.mark.parametrize("a,b,expected", [
    (16, 14, 16),
    (5, 10, 10),
    (-1, -5, -1),
    (0, 0, 0),
    (-10, 10, 10),
])
def test3(a, b, expected):
    assert max_of_two(a, b) == expected


# Exercise 4
@pytest.mark.parametrize("a,b,c,d,expected", [
    (85, 75, 96, 69, 181),
    (81, 82, 83, 84, 330),
    (80, 80, 80, 80, 0),
    (100, 50, 90, 10, 190),
    (1, 2, 3, 4, 0),
])
def test4(a, b, c, d, expected):
    assert sum_greater_than_80(a, b, c, d) == expected


# Exercise 5 (PRINT)
@pytest.mark.parametrize("n,expected_output", [
    (1, "IOI\n"),
    (3, "IOI\nIOI\nIOI\n"),
    (0, ""),
])
def test5(capsys, n, expected_output):
    print_ioi(n)
    captured = capsys.readouterr()
    assert captured.out == expected_output
    assert check_contains_loop(print_ioi)


# Exercise 6 (RETURN)
@pytest.mark.parametrize("n,expected", [
    (0, 1),
    (1, 1),
    (5, 120),
    (7, 5040),
])
def test6(n, expected):
    assert factorial(n) == expected


# Exercise 7 (PRINT)
def test7(capsys):
    expected_output = (
        "3*1=3\n"
        "3*2=6\n"
        "3*3=9\n"
        "3*4=12\n"
        "3*5=15\n"
        "3*6=18\n"
        "3*7=21\n"
        "3*8=24\n"
        "3*9=27\n"
        "3*10=30\n"
    )

    multiplication_table(3)
    captured = capsys.readouterr()
    assert captured.out == expected_output
    assert check_contains_loop(multiplication_table)


# Exercise 8 (PRINT)
def test8(capsys):
    expected_output = (
        "1 \n"
        "2 2 \n"
        "3 3 3 \n"
        "4 4 4 4 \n"
        "5 5 5 5 5 \n"
    )

    print_pattern(5)
    captured = capsys.readouterr()
    assert captured.out == expected_output
    assert check_contains_loop(print_pattern)
