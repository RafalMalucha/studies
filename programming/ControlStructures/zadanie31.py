import random

amount = int(input("How many random numbers do you need:  "))

mn = int(input("Min value of a random number: "))

mx = int(input("Max value of a random number: "))
for i in range(1, (amount + 1)):
    a = random.randint(mn, mx)
    print(a)