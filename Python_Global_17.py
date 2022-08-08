l = 10  # Global Variable


def func1(n):
    global l  # Gives Permission TO Change Value Of Global Variable.
    l = 5 + l  # Local Variable.
    print(n, "I Have Printed")
    print(l)


func1("Helo World!!")
print(l)


def parent():
    x = 5

    def child():
        global x
        x = 84

    print("Before Calling Child()", x)
    child()
    print("after Calling Child()", x)


parent()
