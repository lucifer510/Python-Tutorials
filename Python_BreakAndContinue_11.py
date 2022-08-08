i = 0

while (True):
    if (i + 1 < 5):
        i = i + 1
        continue  # Skip The Step
    print(i + 1, end=" ")
    if (i == 45):
        i = i + 1
        break  # Stop The Loop
    i = i + 1

# QUIZ
while (True):
    num = int(input(print("Enter The Number: \n")))
    if num < 100:
        continue
    elif num > 100:
        print("Congratulations!! You Entered Number Greater than 100....")
        break
