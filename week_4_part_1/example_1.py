def num_days_helper(month: int, is_leap_year: bool) -> int:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year else 28
    else:
        raise ValueError("Invalid month")


def num_days(month: int ,year : int ) ->int:
    is_leap_year = (year % 4 == 0)
    return num_days_helper(month, is_leap_year)

print(num_days(2, 2020))  # Output: 29