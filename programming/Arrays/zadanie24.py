array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

array_greater = []

number = int(input("number: "))

for i in range(len(array)):
    if array[i] > number:
        array_greater.append(array[i])
    else:
        continue
    
print(array_greater)
