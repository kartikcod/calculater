first = input("Enter first number: ")
operater=input("Enter operator /*-+ :")
second= input("Enter Second Number:")

first=int(first)
second=int(second)

if operater == '-':
    print(first-second)
elif operater == '*':
    print(first * second)
elif operater == '/':
    print(first / second)
elif operater == '+':
    print(first + second)

else:
    print("Invalid operator")

