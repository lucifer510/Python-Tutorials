grocery = ["Harpic", "Maggie", "Shampoo", "Lollipop", "GelPen"]  # Making List
print(grocery)  # Printing The List

numbers = [55, 44, 66, 99, 84, 565, 65, 3, 85, 564, 87, 54, 566, 456]

# List Methods
print(numbers)
numbers.reverse()  # Reverse The List
print(numbers)
numbers.sort()  # Sort The List
print(numbers)

# Slicing The List
print(numbers[0:4])  # Print List Including 0 & Excluding 4
print(len(numbers))  # Get Length Of List

# Advance Slicing
print(numbers[0:20:2])  # Print List Excluding 20 While Skipping the Every 2nd Character
print(numbers[0::2])  # Print Full List While Skipping the Every 2nd Character
print(numbers[::2])  # Print Full List While Skipping the Every 2nd Character
print(numbers[::])  # Print Full List
print(numbers[-27::])  # Print Full List
print(numbers[::-1])  # Print Full List In Reverse

print(max(numbers))  # Give The Max Element From The List
print(min(numbers))  # Give The Min Element From The List

# Method Modifying The List
numbers.append(5)  # Add Element In The List At Last
numbers.insert(4, 45)  # Add Element At Given Index
print(numbers)
numbers.remove(5)  # Remove Element From The List
numbers.pop(3)  # Remove Element From The List From Given Index
print(numbers)
numbers[1] = 98  # Replace The Element With Given Element atGiven Index
print(numbers)

# **********TUPLE*********
# Tuple Is Immutable i.e Can't change it's value
tp = (5, 64, 8, 9)  # Creating Tuple
print(tp)
a = 1
b = 8
print(a, b)
a, b = b, a  # Swapping The Element
print(a, b)
