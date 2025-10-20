def has_odd(data : list)-> bool:
    for item in data:
        if type(item) == int and item % 2 :
            return True
    return False

print(has_odd(['0' , 0.0 , -1 ]))