import random

def rand_elem(array):
    x = random.randint(0 ,len(array) - 1)
    return array[x]

print(rand_elem([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
print(rand_elem([24,5125,613,2346,262]))
print(rand_elem([4, 36, 12, 28, 9, 44, 5]))
