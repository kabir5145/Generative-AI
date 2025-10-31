def num_digits(n:int)-> int:
    """Count the total number of digits in n.
    >>> num_digits(37)
    2
    """
    return(len(str(n)))

print(num_digits(-3))