def primes(data: list[int]) -> list[int]:
    """Return a list of all prime numbers in data.
    >>> primes([2,3,4,5])
    [2, 3, 5]
    >>> primes([4,6,8])
    []
    """

    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for i in data:
        if is_prime(i):
            result.append(i)
    return result

print(primes([2, 3, 4, 5]))
