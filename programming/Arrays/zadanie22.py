array = [5125,12351,6147,417347]

def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

diffMinMax = bubblesort(array)[len(array) - 1] - bubblesort(array)[0]

print(diffMinMax)