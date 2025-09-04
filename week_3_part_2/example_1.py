def is_multiple (n : int , m : int) -> bool :
    if m == 0 :
        return False
    return n % m == 0

a = int ( input ("Enter first integer: ") )
b = int ( input ("Enter second integer: ") )

if is_multiple (a , b) :
    print (f"{a} is a multiple of {b}")
else :
    print (f"{a} is not a multiple of {b}")