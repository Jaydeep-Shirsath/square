def cu():
    cube()
def cube():
    num1 = int(input("Enter Your Number: "))
    num2 = num1**3
    print(num2)
    if num2 == num1**3:
        cu()
cube()    