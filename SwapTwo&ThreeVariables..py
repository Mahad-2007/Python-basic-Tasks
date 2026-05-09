#Program Swap two & three variables

#Two Variables
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# print("<---Before Swapping--->")
# print(a, "=", b)

# print("<---After Swapping--->")
# print(b, "=", a)

#Three variables
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("<---Before Swapping--->")
print(a,"=", b)

temp = a
a = b
b = temp

print("<---After Swapping--->")
print(a, "=", b)