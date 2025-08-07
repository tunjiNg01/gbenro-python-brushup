print("a program to check if a number is odd or even")
#getting input from user
num=int(input("enter a number: "))

#check if number is odd or even
if num % 2==0:
    print("{} is even. ".format(num))
else:
    print("{} is odd. ".format(num))