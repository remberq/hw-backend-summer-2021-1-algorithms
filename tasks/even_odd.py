__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    even = sum([value for value in arr if not value % 2])
    odd = sum([value for value in arr if value % 2])
    if not odd:
        return 0
    return even / odd
