def lowercase_vowels(s: str) -> int:
    s = s.lower()
    result = 0
    if 'a' in s:
        result += 1
    if 'e' in s:
        result += 1
    if 'i' in s:
        result += 1
    if 'o' in s:
        result += 1
    if 'u' in s:
        result += 1
    return result   # moved outside the last if


# Example usage
print(lowercase_vowels("Hello World"))   # Output: 2 ('e' and 'o')
print(lowercase_vowels("Python"))        # Output: 1 ('o')
print(lowercase_vowels("AEIOU"))         # Output: 5
