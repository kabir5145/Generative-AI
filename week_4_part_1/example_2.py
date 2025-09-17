def sum_to(n: int) -> int:
    """Calcultate 1+2+...+n 
    >>> sum_to(4)
    10
    >>> sum_to(-1)
    0
    """

    if n < 1:
        return 0
    return (n * (n + 1)) // 2


print(sum_to(4))   # 10
print(sum_to(-3))  # 0