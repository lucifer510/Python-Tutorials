# Lambda Functions
def add(a, b):
    return a + b


minus = lambda x, y: x - y

print(minus(9,4))
a = [[1, 4], [5, 6], [4, 3]]
a.sort(key=lambda x:x[1])
print(a)