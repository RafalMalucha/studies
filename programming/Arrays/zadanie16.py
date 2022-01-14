array = [12, 6, 4, 9, 3]

def star(n):
    return "*" * array[n]

for n in range(len(array)):
    print(star(n))
    