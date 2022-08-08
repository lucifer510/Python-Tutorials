# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)


def fun(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    print("\nNow I Will Introduce My Team Members!!")
    for key, Value in kwargs.items():
        print(f"{key} is learning {Value}")


# function_name_print("Mihir", "Mobin", "Raj", "Yashvi", "Vrushti")
kw = {"Mihir": "ADA", "Mobin": "CN", "Yashvi": "SE", "Vrushti": "PDS"}
list = ["Mihir", "Mobin", "Raj", "Yashvi", "Vrushti"]
normal = "I Am A Normal Argument & The Students Are "
fun(normal, *list, **kw)
