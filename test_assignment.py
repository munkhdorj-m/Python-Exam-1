import pytest,inspect
from assignment import *

def check_contains_loop(func):
    source = inspect.getsource(func)
    return "for " in source or "while " in source
    
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

@pytest.mark.parametrize("y,m,expected", [
    (2, 7, 31),
    (0, 5, 5),
    (1, 0, 12),
    (10, 0, 120),
    (0, 0, 0),
])
def test2(y, m, expected):
    assert years_months_to_months(y, m) == expected

@pytest.mark.parametrize("a,b,expected", [
    (16, 14, 16),
    (5, 10, 10),
    (-1, -5, -1),
    (0, 0, 0),
    (-10, 10, 10),
])
def test3(a, b, expected):
    assert max_of_two(a, b) == expected

@pytest.mark.parametrize("a,b,c,d,expected", [
    (85, 75, 96, 69, 181),
    (81, 82, 83, 84, 330),
    (80, 80, 80, 80, 0),
    (100, 50, 90, 10, 190),
    (1, 2, 3, 4, 0),
])
def test4(a, b, c, d, expected):
    assert sum_greater_than_80(a, b, c, d) == expected

@pytest.mark.parametrize("n,expected_output", [
    (1, "IOI\n"),
    (3, "IOI\nIOI\nIOI\n"),
    (0, ""),
])
def test5(capsys, n, expected_output):
    print_ioi(n)
    captured = capsys.readouterr()
    assert captured.out == expected_output

@pytest.mark.parametrize("n,expected_output", [
    (0, "1\n"),
    (1, "1\n"),
    (5, "120\n"),
    (7, "5040\n"),
])
def test6(capsys, n, expected_output):
    factorial(n)
    captured = capsys.readouterr()
    assert captured.out == expected_output

def test7():
    expected = [
        "3*1=3",
        "3*2=6",
        "3*3=9",
        "3*4=12",
        "3*5=15",
        "3*6=18",
        "3*7=21",
        "3*8=24",
        "3*9=27",
        "3*10=30",
    ]
    assert multiplication_table(3) == expected


def test8(capsys):
    expected_output = (
        "1 \n"
        "2 2 \n"
        "3 3 3 \n"
        "4 4 4 4 \n"
        "5 5 5 5 5 \n"
    )
    print_pattern_1(5)
    captured = capsys.readouterr()
    assert captured.out == expected_output
    assert check_contains_loop(print_pattern_1)
