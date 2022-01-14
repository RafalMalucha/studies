array = [2,4,21,1,15,52]

def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
                

print(bubblesort(array))

secondLargest = bubblesort(array)[len(array) - 2]

print(secondLargest)