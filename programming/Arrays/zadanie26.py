array = [2,4,21,1,15,52]

def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def arrayEvenOdd(array):
    array = bubblesort(array)
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] % 2 == 0:
                if array[j + 1] % 2 == 0:
                    continue
                if array[j + 1] % 2 != 0:
                    continue
            if array[j] % 2 != 0:
                if array[j + 1] % 2 == 0:
                    array[j], array[j + 1] = array[j + 1], array[j]
                if array[j + 1] % 2 != 0:
                    continue
    return array

print(arrayEvenOdd(array))
                
                    
