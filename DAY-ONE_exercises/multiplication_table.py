print("program to print multiplication table from 1 to 12")

#print header row
print(" ", end="")
for i in range(1,13):
    print(f'{i:4}', end="")
print('\n' + "-"* 52)

#print each row of the table
for row in range(1,13):
    print(f'{row:2} |', end="") #row header with a seperator
    for col in range(1,13): 
        print(f'{row* col:4}', end="")
    print() #move to the next row