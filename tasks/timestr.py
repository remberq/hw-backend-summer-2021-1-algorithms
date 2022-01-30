__all__ = (
    'seconds_to_str',
)
import time

def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    if seconds < 60:
        return time.strftime('%Ss', time.gmtime(seconds))

    if 60 <= seconds < 3600:
        return time.strftime('%Mm%Ss', time.gmtime(seconds))

    if 3600 <= seconds < 86400:
        return time.strftime('%Hh%Mm%Ss', time.gmtime(seconds))

    if seconds >= 86400:
        day = int(seconds / 86400)
        if day > 9:
            return time.strftime(f'{day}d' + '%Hh%Mm%Ss', time.gmtime(seconds))
        return time.strftime(f'0{day}d' + '%Hh%Mm%Ss', time.gmtime(seconds))




