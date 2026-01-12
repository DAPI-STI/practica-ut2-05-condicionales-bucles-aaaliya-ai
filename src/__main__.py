"""
Archivo principal del proyecto.

Desde aquí puedes probar las funciones SIN usar pytest.
Este archivo NO se evalúa automáticamente.
"""

from ex01_sign import sign
from ex02_leap_year import is_leap_year
from ex03_sum_first_n import sum_first_n
from ex04_factorial import factorial
from ex05_table import multiplication_table
from ex06_fizzbuzz import fizzbuzz


def main() -> None:
    print("=== Pruebas manuales ===")
    print("sign(-3) ->", sign(-3))
    print("is_leap_year(2000) ->", is_leap_year(2000))
    print("sum_first_n(10) ->", sum_first_n(10))
    print("factorial(5) ->", factorial(5))
    print("multiplication_table(3) ->", multiplication_table(3))
    print("fizzbuzz(15) ->", fizzbuzz(15))


if __name__ == "__main__":
    main()
