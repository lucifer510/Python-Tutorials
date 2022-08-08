# If Else Example --> Take 3 User input Number And Print Greatest Number Among Them
print("Enter Value Of A:")
a = input()
print("Enter Value Of B:")
b = input()
print("Enter Value Of C:")
c = input()

if (a > b) and (a > c):
    print(a, "Is Greatest Number Among 3")
elif (b > a) and (b > c):
    print(b, "Is Greatest Number Among 3")
else:
    print(c, "Is Greatest Number Among 3")
