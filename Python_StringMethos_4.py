myStr = "Hello Mihir, Good Morning!!"
print(myStr)

# Slicing The String
print(myStr[0:4])  # Print String Including 0 & Excluding 4
print(len(myStr))  # Get Length Of String

# Advance Slicing
print(myStr[0:20:2])  # Print String Excluding 20 While Skipping the Every 2nd Character
print(myStr[0::2])  # Print Full String While Skipping the Every 2nd Character
print(myStr[::2])  # Print Full String While Skipping the Every 2nd Character
print(myStr[::])  # Print Full String
print(myStr[-27::])  # Print Full String

print(myStr[::-1])  # Print Full String In Reverse

# String Method
print(myStr.isalnum())  # Return True String Is Alpha Numeric
print(myStr.isalpha())  # Return True if String Is Alpha
print(myStr.count("M"))  # Count How Many Times Given Character Is Occurred
print(myStr.__contains__("r"))  # Return True If String Contains Given Character
print(myStr.swapcase())  # Swap The Case Of The String
print(myStr.center(50, '*'))  # Centralize The String And Fill Empty Space With Given Character
print(myStr.lower())  # Convert String Into Lower Case
print(myStr.upper())  # Convert String Into Upper Case
print(myStr.replace("Morning", "Afternoon"))  # Replace The Characters
