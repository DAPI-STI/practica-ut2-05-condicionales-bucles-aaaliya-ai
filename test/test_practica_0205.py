import pytest

from src.ex01_sign import sign
from src.ex02_leap_year import is_leap_year
from src.ex03_sum_first_n import sum_first_n
from src.ex04_factorial import factorial
from src.ex05_table import multiplication_table
from src.ex06_fizzbuzz import fizzbuzz


def test_ex01_sign():
    assert sign(10) == "positivo"
    assert sign(-1) == "negativo"
    assert sign(0) == "cero"


def test_ex02_leap_year():
    assert is_leap_year(2000) is True
    assert is_leap_year(1900) is False
    assert is_leap_year(2024) is True
    assert is_leap_year(2023) is False


def test_ex03_sum_first_n():
    assert sum_first_n(1) == 1
    assert sum_first_n(5) == 15
    assert sum_first_n(0) == 0
    assert sum_first_n(-3) == 0


def test_ex04_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)


def test_ex05_table():
    assert multiplication_table(3) == [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]


def test_ex06_fizzbuzz():
    assert fizzbuzz(0) == []
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert fizzbuzz(15)[-1] == "FizzBuzz"
