str = "Guess The Number"

print(str.center(50,"*"))

i = 1
num = 18
while (True):
    gnum = int(input(print("Guess The Number: \n")))
    if num == gnum:
        print("Congratulations!! You've Guessed Correct Number in attempt",i)
        i = i + 1
        break
    elif num > gnum:
        print("Sorry :( Your Number is less Than Correct Number Try Again")
        i = i + 1
        continue
    elif num < gnum:
        print("Sorry :( Your Number Is Greater Than Correct Number Try Again")
        i = i + 1
        continue

