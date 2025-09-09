def num_days(month: int , is_leap: bool) -> int:
    """Return the number of days in month.
    month is an integer in the range 1...12.
    is_leap is True if it is a leap year, False otherwise.
    >>> num_days(2, False)
    28
    >>> num_days(2, True)
    29
    >>> num_days(4, False)
    30
    >>> num_days(12, False)
    31
    """
    if month == 2:
        if is_leap:
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31