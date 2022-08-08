# Dictionary is nothing but key value pairs

d1 = {}  # Empty Dictionary
print(type(d1))  # To Get Type

d2 = {"Mihir": "Momos", "Raj": "Chicken", "Manoj": "Pakodi",
      "Sonal": {"BreakFast": "Tea", "Lunch": "Sabji-roti", "Dinner": "Pizza"}}  # Making Dictionary
print(d2)  # Printing Dictionary

print(d2["Mihir"])  # Printing Specific Element From Dictionary
print(d2["Sonal"]["BreakFast"])  # Printing Specific Element From Dictionary
d2["Rohan"] = "Chinese"  # Add Element In Dictionary
d2["Kashish"] = "Maggie"  # Add Element In Dictionary
print(d2)
del d2["Rohan"] # Remove Element From Dictionary
print(d2)

d1 = d2.copy() # Copy Data Of Dictionary
print(d1.get("Mihir"))
d1.update({"Leena":"Toffee"}) # To Update The Dictionary
print(d1)