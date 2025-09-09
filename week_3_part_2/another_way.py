def num_days(month, year):
    if not (1 <= month <= 12):
        return 0
    
    # Leap year check
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    
    if month == 2:
        return 29 if is_leap else 28
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    return 31