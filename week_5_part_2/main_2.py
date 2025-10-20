def first_positive(data : list[int]) -> int:
    """ Retrun the first positive integer in a data.
    >>> first_positive([-2,3,1])
    3
    >>> first_positive([-2,-3,-1])
    0
    """

    for x in data:
        if x > 0:
            return x
    return "There is no positive integer in the list."

print(first_positive([-2,3,1]))
print(first_positive([-2,-3,-1]))