#Program Largest amon three numbers

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

largest = a
if(a > b):
    print(a, "is largest")
elif(b > c):
    print(b, "is largest")
else:
    print(c, "is largest")