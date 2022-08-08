list1 = [["Robin", 12], ["Carry", 31], ["Mihir", 20], ["Raj", 16]]
# For Loop
for item, age in list1:
    print(item, "and His Age is", age)

dict1 = dict(list1)  # Covert List In to Dictionary
for item in dict1:
    print(item)  # Print Only Keys From Dictionary
for item, age in dict1.items():
    print(item, "and His Age is", age)

list2 = ["Mihir", 5, "Robin", 12, 87, 42]

for item in list2:
    if str(item).isnumeric() and item < 50 :
        print(item)
