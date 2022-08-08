def fectorial_recursive(n):
    """
    This Method Gives Factorial By Recursive Approach
    :param n:
    :return:
    """
    if n == 1:
        return 1
    else:
        return n * fectorial_recursive(n - 1)


def factorial_iterative(n):
    """
    This Method Gives Factorial By Iterative Approach
    :param n:
    :return:
    """
    ans = 1
    for i in range(n, 0, -1):
        ans = ans * i
    return ans


n = int(input("Please Enter The Number: "))

print("Factorial By Recursive Approach : ", fectorial_recursive())
print("Factorial By Iterative Approach : ", factorial_iterative())
