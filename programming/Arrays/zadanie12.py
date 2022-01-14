array = [15, 8, 31, 47, 2, 19]

array_2 = []

for i in range((len(array) - 1), -1, -1):
    array_2.append(array[i])
    
print("existed array: ", *array)
print("reversed array: ", *array_2)
    