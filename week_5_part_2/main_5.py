def vowel_count(s: str) -> int:
    """ Return the number of vowels in a string.
    >>> vowel_count("hello")
    2
    >>> vowel_count("sky")
    0
    """

    count = 0
    for char in s:
        if char.lower() in 'aeiou':
            count += 1
    return count

print(vowel_count(input("Enter a string: ")))