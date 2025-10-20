def mystery(data : list) -> bool:
    if data == []:
        return False
    if data[0]%2:
        return True
    return mystery(data[1:])

print(mystery([0.0, -1 , '0']))