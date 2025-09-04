def median(a:int, b:int, c:int) -> int:
    """Calculate the median of 3 ints.
       median(1,2,3)
       median(9,3,6)
       median(7,8,0)
       """
    if a <= b <= c:
        return b
    elif b <= a <= c:
        return a
    else:
        return c
    
    print(median(a,b,c))
    