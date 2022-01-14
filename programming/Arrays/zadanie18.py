def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
                
                
print(bubblesort([15, 38, 7, 23, 14]))
print(bubblesort([24,5125,613,2346,262]))
print(bubblesort([1251325,235236,2623623,23626]))