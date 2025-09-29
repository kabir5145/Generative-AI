def num_digits(n: int)-> int: 

    """Count the number of digits in n .
    >>> num_digits(37)
    2
    >>> num_digits(100)
    3
    """
    n = abs(n)  # handle negative numbers
    if n <= 9 :
        return 1
    return 1 + num_digits(n//10)
print(num_digits(-37))