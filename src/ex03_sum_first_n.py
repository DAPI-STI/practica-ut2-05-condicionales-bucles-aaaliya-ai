"""
Ejercicio 3:
Suma de los primeros n números.
"""

def sum_first_n(n: int) -> int:
    """
    Devuelve la suma 1 + 2 + ... + n.

    - Si n <= 0, devuelve 0.
    - Debe resolverse usando un bucle (for o while).
    """
    if n <= 0:
        return 0

    total = 0
    for i in range(1, n + 1):
        total += i

    return total
