import random

print("guess the number rolled")

a = random.randint(1, 6)

b = int(input("guess: "))

if a == b:
    print("True")
elif b > 6:
    print("think again how many sides does dice have")
elif b < 1:
    print("think again how many sides does dice have")
else:
    print("no.")
    
input("Press enter to exit ;)")
