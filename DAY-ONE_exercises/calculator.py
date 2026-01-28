def user_info():
    global name
    name=input(" Enter your name pls: ")
    print("Hello {} ,welcome to gbenro's mini calculator session. ".format(name))
user_info()

def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    return x/y

def power(x,y):
    return x**y

def square_root():
    square_value=int(input(" Enter the root value: "))
    initial_value=int(input(" Enter the initial value: "))
    new_const1=1
    complex_root_value=new_const1/square_value
    return pow(initial_value,complex_root_value)

def calculator():
    first_value=float(input(" Enter the first value: "))
    second_value=float(input(" Enter the second value: "))
    operation=input(" Enter an operation(either +,-,*,/,^,sqr): ")
    if operation=="+":
        print("the addition of the two values is ",addition(x=first_value,y=second_value))
    elif operation=="-":
        print("the subtraction of the two values is ",subtraction(x=first_value,y=second_value))
    elif operation=="*":
        print("the multiplication of the two values is ",multiplication(x=first_value,y=second_value))
    elif operation=="/":
        print("the division of the two values is ",division(x=first_value,y=second_value))
    elif operation=="^":
        print("your first value raised to power of the second value is ",power(x=first_value,y=second_value))
    elif operation=="sqr":
        print("the square root of the initial value  is ",square_root())
    else:
        print(" Dear {} ,Pls enter a valid operation".format(name))
calculator()