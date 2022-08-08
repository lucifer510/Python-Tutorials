# Faulty Calculator

# 45*3=555,56+9=546,87-2=42

a = int(input(print("Enter Value Of A:")))
op = (input(print("Enter Which Operation Do you Want To Do:")))
b = int(input(print("Enter Value Of B:")))

if (a == 45) and (b == 3) and (op == "*"):
    print("555")
elif (a == 56) and (b == 9) and (op == "+"):
    print("546")
elif (a == 87) and (b == 2) and (op == "-"):
    print("42")
elif op == "+":
    print(a+b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif (op == "/") and (a > b) and (b != 0):
    print(a / b)
else:
    print("Syntax Error!")
