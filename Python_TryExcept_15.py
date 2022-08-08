num1 = (input(print("Enter Num1: \n")))
num2 = (input(print("Enter Num2: \n")))

try:
    print("sum of these 2 numbers", int(num1) + int(num2))
except Exception as e:
    print(e)

print("This Line Has to Print")
