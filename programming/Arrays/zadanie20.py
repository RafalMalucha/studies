def occurs(number, array):
    for i in range(len(array)):
        if number == array[i]:
            return True
        else:
            continue
        
number = int(input("Number:" ))

if occurs(number, [15, 38, 7, 23, 14]) == True:
    print(f"Number {number} appears in the array")
else:
    print(f"Number {number} does not appear in the array")