array =  [1,7,9,4,6,8]

def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def median(array):
    array = bubblesort(array)
    if len(array) % 2 != 0:
        mid = int(len(array) // 2)
        median = array[mid]
        return median
    else:
        mid1 = int(len(array) // 2) - 1
        mid2 = int(len(array) // 2) 
        median = (array[mid1] + array[mid2]) / 2
        return median
    


print(median(array))