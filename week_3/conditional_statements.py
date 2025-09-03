def is_multiple(n: int,m: int)-> bool:
    """Check if n is a multiple of m.
    is_multiple(10,5)  # True
    is_multiple(10,0)  # False
    return n % m == 0"""
    if m == 0:  # prevent ZeroDivisionError
        return False
    return n % m == 0
    print(is_multiple(10,5)) 
    print(is_multiple(10,0))