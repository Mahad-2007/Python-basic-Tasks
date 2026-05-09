# Program Celsisus to fahrenheit and kelvin

cel = int(input("Enter temperature in celsius: "))

fahrenheit = (cel * (9/5)) +32
kelvin = cel + 273.15

print(f"{cel} celsius is equal to {fahrenheit} fahrenheit.")
print(f"{cel} celsius is equal to {kelvin} kelvin.")