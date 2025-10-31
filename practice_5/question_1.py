def first_word(s:str)->str:
    try:
        s = s.split()
        return s[0]
    except IndexError:
        return ''
print(first_word('August 15,1947'))
