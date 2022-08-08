# Game:- Snake, Water, Gun
import random

print("Snake--Water--Gun".center(200, "-"))
rounds = int(input("Enter How Many Round Do You Want To Play :\n"))
i = 1
me = 0
pc = 0
while i <= rounds:
    print(f"Round-{i}".center(200, "-"))
    # print(f"me :- {me}".right)
    print("1.Snake")
    print("2.Water")
    print("3.Gun")
    myChoice = int(input("Please Enter Your Choice"))
    computerChoice = random.randint(1, 3)
    print(f"Computer's Choice Is : {computerChoice}")
    if ((myChoice == 1) and (computerChoice == 2)) or ((myChoice == 2) and (computerChoice == 3)) or (
            (myChoice == 3) and (computerChoice == 1)):
        print(f"Congratulations!! You Win Round - {i}")
        me = me + 1
    elif ((myChoice == 1) and (computerChoice == 3)) or ((myChoice == 2) and (computerChoice == 1)) or (
            (myChoice == 3) and (computerChoice == 2)):
        print(f"Sorry :( You Lose Round - {i}")
        pc = pc + 1
    else:
        print(f"Round - {i} Is A Draw...")
    print(f"Score After Round - {i} is \n You - {me} \n pc - {pc}")
    i = i + 1
if me > pc:
    print("Congratulations!! You Win The Game..")
else:
    print("Sorry :( You Lose The Game..")
