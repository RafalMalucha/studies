import random

array = []

string = ""

for i in range(1, 1000):
    array.append(i)

print("-" * 50)

for j in range(1, 8):
    x = random.randint(1, 999)
    string += "|  " + str(array[x])

for k in range(8, 9):
    x = random.randint(1, 999)
    string += "|  " + str(array[x]) + "|"
    
print(string)
        
print("-" * 50)
        