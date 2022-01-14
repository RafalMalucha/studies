ints_1 = [4, 36, 12, 28, 9, 44, 5]

ints_2 = [5, 1, 36]

for i in range(len(ints_1)-1):
    for j in range(len(ints_2)-1):
        if ints_1[i] == ints_2[j]:
            ints_1.pop(i)
        else:
            continue
            
            
print(ints_1)
        