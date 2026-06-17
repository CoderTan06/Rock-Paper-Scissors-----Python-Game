#Basic Calculator Program - TS
num1 = float(input("Enter your first number : "))
operation = input("What operation do you want to use? (+,-,*,/) : ")
num2 = float(input("Enter your second number : "))

if operation == "+" :
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/":
    if num2 == 0:
        print("Error : number cannot be divided zero")
    else:
        print(num1/num2)
else:
    print("Invalid operation")
