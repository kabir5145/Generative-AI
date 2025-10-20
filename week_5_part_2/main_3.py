def first_vowel(s: str) -> str:
    """ Return the first vowel in a string.
    >>> first_vowel("hello")
    'e'
    >>> first_vowel("sky")
    'There is no vowel in the string.'
    """

    for char in s:
        if char.lower() in 'aeiou':
            return char
    return "There is no vowel in the string."

print(first_vowel(input("Enter a string: ")))