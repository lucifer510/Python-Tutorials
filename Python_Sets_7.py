s = set()  # Empty Set
print(type(s))  # Print Type Of Variable
s_from_list = set([1, 2, 3, 4])
print(s_from_list)

# Add Element In Set
s.add(5)
s.add(6)
s.add(5)  # Set Only Contains Unique Element
s.add(58)
s.add(98)
print(s)  # Printing Elements Of Set
s1 = s.union({1,6,8,4}) # does Union with set s
print(s1)
s2 = s.intersection({1,6,8,4}) # does intersection with set s
print(s2)
print(len(s)) # Print Length Of set
s.remove(5) # Remove Element From set
print(s)