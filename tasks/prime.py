__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    if number < 2:
        return False
    for value in range(2, number):
        if not number % value:
            return False
    return True
