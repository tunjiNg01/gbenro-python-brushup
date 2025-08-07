
def division(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return "Error: cannot divide by zero!"
    
def main():
    dividend=int(input("Enter the dividend value: "))
    divisor=int(input("Enter the value for the divisor: "))
    print("The division for the two values is: ",division(x=dividend,y=divisor))
main()   