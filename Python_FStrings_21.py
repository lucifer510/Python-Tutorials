# F Strings
import math

me = "Mihir"
a1 = 3
a = "This is %s" % me
print(a)
a = "This is {} {}"
b = a.format(me, a1)
print(b)
c = f"This is {me} {a1} {math.cos(45)}"  # --> F String
print(c)
