def prime_product(data : list[int]) -> int:
    """ Return the product of all prime numbers in data.
    >>> prime_product([2,3,4,5])
    30
    >>> prime_product([4,6,8])
    1
    """

    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    product = 1
    found_prime = False
    for x in data:
        if is_prime(x):
            product *= x
            found_prime = True

    return product if found_prime else 1

print(prime_product([2,3,4,5]))
print(prime_product([4,6,8]))