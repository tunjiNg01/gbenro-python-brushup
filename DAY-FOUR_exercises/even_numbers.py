
with open("even_numbers.txt", "w") as file:
    file.write("a program to log all even numbers unto a file. \n")
    even_number= 0
    for even_number in range(1,101,1):
        if even_number % 2 ==0:
            file.write(str(even_number)+ "\n")

print("even numbers logged sucessfully.")