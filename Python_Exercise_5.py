# Health Management System
# 3 Clients - Mihir,Raj,Manoj
def log():
    """This Function Use For Write Data In File"""
    print("Please Write Below Your Content : ")
    f.write(input())
    f.write("\n")


def retrive():
    """This Function Use For Read Data From File"""
    for line in f:
        print(line, end=" ")
    print()


b = True
while b:
    # Main Menu Of HMS
    print("Health Management System".center(200, "-"))
    print("Enter The Number Whose File Do You Want To Manage : ")
    print("1. Mihir")
    print("2. Raj")
    print("3. Manoj")
    print("0. Exit")
    choice = int(input())

    # Choices From Main Menu
    if choice == 0:  # Code For Exit HMS
        exit()
    elif choice == 1:  # Code For Choice 1 -- Mihir
        a = True
        while a:
            # Code For Mihir's Menu
            print(" Enter The Number What Do You Want To Manage : ")
            print("1. Diet Plan")
            print("2. Workout Plan")
            print("3. Previous Menu")
            print("0. Exit")
            choice2 = int(input())

            # Choices From Mihir's Menu

            if choice2 == 0:  # Code For Exit
                exit()
            elif choice2 == 1:  # Code For Diet Plan
                c = True
                while c:

                    # Code For Diet Plan Menu
                    print("Enter What Do You Want To Do : ")
                    print("1. Read Diet Plan")
                    print("2. Write Diet Plan")
                    print("3. Previous Menu")
                    print("0. Exit")
                    choice3 = int(input())

                    # Choices From Diet Plan Menu
                    if choice3 == 0:  # Code For Exit
                        exit()
                    elif choice3 == 1:  # Code For Read Diet Plan
                        with open("Mihir Diet plan.txt ") as f:
                            retrive()
                    elif choice3 == 2:  # Code For Update Diet Plan
                        with open("Mihir Diet plan.txt ", "a") as f:
                            log()
                    elif choice3 == 3:
                        break
            elif choice2 == 2:  # Code For Workout Plan
                c = True
                while c:

                    # Choices For Workout Plan Menu
                    print("Enter What Do You Want To Do : ")
                    print("1. Read Workout Plan")
                    print("2. Write Workout Plan")
                    print("3. Previous Menu")
                    print("0. Exit")
                    choice3 = int(input())

                    # Choices From WorkOut Plan
                    if choice3 == 0:  # Code For Exit
                        exit()
                    elif choice3 == 1:  # Code For Reading WorkOut Plan
                        with open("Mihir Workout plan.txt") as f:
                            retrive()
                    elif choice3 == 2:  # Code For Update WorkOut Plan
                        with open("Mihir Workout plan.txt", "a") as f:
                            log()
                    elif choice3 == 3:
                        break
            elif choice2 == 3:
                break
    elif choice == 2:
        a = True
        while a:
            print(" Enter The Number What Do You Want To Manage : ")
            print("1. Diet Plan")
            print("2. Workout Plan")
            print("3. Previous Menu")
            print("0. Exit")
            choice2 = int(input())
            if choice2 == 0:
                exit()
            elif choice2 == 1:
                c = True
                while c:
                    print("Enter What Do You Want To Do : ")
                    print("1. Read Diet Plan")
                    print("2. Write Diet Plan")
                    print("3. Previous Menu")
                    print("0. Exit")
                    choice3 = int(input())
                    if choice3 == 0:
                        exit()
                    elif choice3 == 1:
                        with open("Raj Diet plan.txt ") as f:
                            retrive()
                    elif choice3 == 2:
                        with open("Raj Diet plan.txt ", "a") as f:
                            log()
                    elif choice3 == 3:
                        break
            elif choice2 == 2:
                c = True
                while c:
                    print("Enter What Do You Want To Do : ")
                    print("1. Read Workout Plan")
                    print("2. Write Workout Plan")
                    print("3. Previous Menu")
                    print("0. Exit")
                    choice3 = int(input())
                    if choice3 == 0:
                        exit()
                    elif choice3 == 1:
                        with open("Raj Workout plan.txt ") as f:
                            retrive()
                    elif choice3 == 2:
                        with open("Raj Workout plan.txt ", "a") as f:
                            log()
                    elif choice3 == 3:
                        break
            elif choice2 == 3:
                break
    elif choice == 3:
        a = True
        while a:
            print(" Enter The Number What Do You Want To Manage : ")
            print("1. Diet Plan")
            print("2. Workout Plan")
            print("3. Previous Menu")
            print("0. Exit")
            choice2 = int(input())
            if choice2 == 0:
                exit()
            elif choice2 == 1:
                c = True
                while c:
                    print("Enter What Do You Want To Do : ")
                    print("1. Read Diet Plan")
                    print("2. Write Diet Plan")
                    print("3. Previous Menu")
                    print("0. Exit")
                    choice3 = int(input())
                    if choice3 == 0:
                        exit()
                    elif choice3 == 1:
                        with open("Manoj Diet plan.txt ") as f:
                            retrive()
                    elif choice3 == 2:
                        with open("Manoj Diet plan.txt ", "a") as f:
                            log()
                    elif choice3 == 3:
                        break
            elif choice2 == 2:
                c = True
                while c:
                    print("Enter What Do You Want To Do : ")
                    print("1. Read Workout Plan")
                    print("2. Write Workout Plan")
                    print("3. Previous Menu")
                    print("0. Exit")
                    choice3 = int(input())
                    if choice3 == 0:
                        exit()
                    elif choice3 == 1:
                        with open("Manoj Workout plan.txt ") as f:
                            retrive()
                    elif choice3 == 2:
                        with open("Manoj Workout plan.txt ", "a") as f:
                            log()
                    elif choice3 == 3:
                        break
            elif choice2 == 3:
                break