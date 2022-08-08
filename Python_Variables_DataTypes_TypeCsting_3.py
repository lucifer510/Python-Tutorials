var1 = "hello world"  # String Variable
var2 = 3  # Integer Variable
var3 = 5.10  # Float Variable
var4 = "Mihir Prajapati"
var5 = " 5"
var6 = "10"

# To Print Variable
print(var1)
print(var2)
print(var3)

# To Know Type Of Variable
print(type(var1))
print(type(var2))
print(type(var3))

# To Add Variable
print(var1 + var4)
print(var2 + var3)

# print(var1 + var2)  # Error Line Can't Add Number & String
print(var1 + var5)
print(var6 + var5)
print(int(var6) + int(var5))  # Type Casting To Integer

# Print Somthing N Times
print(10 * "Hello Detective!!\n")  # N = 10
print(100 * int(var6) + int(var5))  # This Will Multipy The Ans With 100 Instead Of Print 100 Times
print(100 * str(int(var6) + int(var5)))  # This Will Work By TypeCasting Ans Into String

# Take User Input
print("Enter How Many Times You Want To Print Same Line?")
n: int = input()
print(int(n) * "Hello Detective!!\n")  # n = UserInput which Is String By Default So We Have To TypeCast It Into Integer
