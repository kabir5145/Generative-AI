def next(n):
    """Return the next even number after n by adding 1 and then another 1 if n is odd. If n is even ,just add the first 1."""
    return n + 1 + (n % 2)