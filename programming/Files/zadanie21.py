import random
file = open("intsRandom.txt", "w")
for i in range(1,51):
    x = str(random.randint(100, 999)) + "\n"
    file.write(x)

file.close()
    