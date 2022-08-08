a = 9
b = 10
c = sum((a, b))  # --> sum is Pre define Function
print(c)


def func1(a, b):  # Define The Function
    print("Hello ! You Are In Function 1", a + b)


def function2(a, b):
    """this is doc string"""
    avg = (a + b) / 2
    # print(avg)
    return avg

func1(5, 6)  # Calling The Function
v = function2(12, 6)
print(v)
print(function2.__doc__) # Printing The Doc String 
