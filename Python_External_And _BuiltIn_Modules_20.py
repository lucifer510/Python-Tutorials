import random

random_num = random.randint(0, 5)
# print(random.__doc__) # Gives Information About random function
# rand = random.random()  # Print Random Number Between 0 & 1.
rand = random.random() * 100  # Print Random Number Between 0 & 100.
# print(random_num)
print(rand)

lst = ["StarPlus", "DD1", "FTV", "BBC", "NetFlix", "DisneyPlus"]
choice = random.choice(lst)
print(choice)

# External Module
from turtle import *

color('black', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
