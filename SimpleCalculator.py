# Program Make a simple calculator

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
op = input("Enter an operator: ")

print("<<---Calculator--->>")
if(op == '+'):
    print(a+b)
elif(op == '-'):
    print(a-b)
elif(op == '*'):
    print(a*b)
elif(op == '/'):
    if(a/b ==0):
        print("infintiy")
    else:
        print(a/b)
    