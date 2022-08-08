# File IO Basics

"""
"r" - Open File For Reading - Default
"w" - Open File For Writing
"x" - Creates File If Not Exists
"a" - Add More Content To File
"t" - Text Mode -
"t" - Text Mode - Default
"b" - Binary Mode
"+" - Read & Write Both
"""

print("Reading From File".center(100, "*"))
f = open("Python.txt", "r")  # --> To Open File

content = f.read()  # --> To read Content
print(content)  # To Print Content

for line in f:
    print(line, end=" ")

print(f.readline())  # --> Read one line, where “line” is a sequence of bytes ending with \n.
print(f.readlines())  # --> Read all lines available on the input stream and return them as a list of lines.
f.close()  # --> To Close File

# Writing In File
print("Writing In File".center(100,"*"))

f = open("Python2.txt", "w")
f.write("Hello! World...\n")
f.writelines("I Am Mihir")  # --> Add Content To File
f.close()

# Handle Read And Write Both In File
print("Handle Read And Write Both In File".center(100,"*"))
f = open("Python2.txt", "r+")
print(f.read())
f.write("Thank You\n")
f.close()

# Seek() And Tell() Functions On Python File
print(" Seek() And Tell() Functions On Python File ".center(100,"*"))
f = open("Python2.txt")
print(f.tell()) # --> Gives Current Position Of File Pointer
print(f.readline())
print(f.tell())
print(f.readline())
f.seek(0)  # --> Set Position Of File Pointer To 0
print(f.tell())
print(f.readline())
f.close()

# Using With Block To Open Python File
print(" Using With Block To Open Python File ".center(100,"*"))
with open("Python2.txt") as f: # Do Job Of f=open("Python2.txt")  And  f.close()
    print(f.readlines())
    a = f.read(5)
    print(a)
