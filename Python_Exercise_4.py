# Pattern Printing

num = int(input(print("Please Enter The Number: \n")))
b = bool(int((input(print("Please Enter The Boolean Value ( 1 = true and 0 = False):")))))
print(b)
if (b == True):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
elif b == False:
    for i in range(num, 0, -1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
