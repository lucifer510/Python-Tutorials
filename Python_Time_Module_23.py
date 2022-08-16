import time

initial = time.time()
print(initial)
for i in range(45):
    print(f"This Is For Loop {i} Time")
    time.sleep(2)  # Pause Program For Particular Seconds..
print(f"For Loop Ran In", time.time() - initial, " Seconds")

initial2 = time.time()
k = 0
while k < 45:
    print(f"This Is While Loop {k} Time")
    k = k + 1
print(f"While Loop Ran In ", time.time() - initial2, " Seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)  # Return Current Date & Time
