print("a program to convert temperature from either celsius to farenheit or farenheit to celsius")

#function handling the conversion from celsius to farenheit
def celsius_to_farenheit(celsius):
    return (celsius * 9/5) + 32


#function handling the conversion from farenheit to celsius
def farenheit_to_celsius(farenheit):
    return (farenheit - 32) * 5/9

def temperature_converter():
    print("=== TEMPERATURE CONVERTER ===")
    print(" 1 for celsius to farenheit")
    print(" 2 for farenheit to celsius")

    choice= input("pick a conversion option(either 1 or 2): ")
    temperature=float(input(" Enter the temperature value: "))

    if choice== "1":
        print(" {}C = {}F".format(temperature,celsius_to_farenheit(celsius=temperature)))
    elif choice== "2":
        print(" {}F = {}C".format(temperature,farenheit_to_celsius(farenheit=temperature)))
    else:
        print("invalid option choose between 1 and 2")
temperature_converter()
