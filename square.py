def y():
    sq()

def sq():
    s = int(input("Enter Your Number: "))
    o = s**2
    print(o)
    if o == s**2:
        y()
sq()         