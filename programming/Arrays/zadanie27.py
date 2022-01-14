def arrayToString(array):
    string = ""
    for i in range(len(array) - 1):
        string += str(array[i]) + ", "
    for i in range(len(array) - 1, len(array)):
        string += str(array[i])
    return string



print(arrayToString([6236,2346,458468,4684684,354734527,2472472]))