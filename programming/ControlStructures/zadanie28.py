x = int(input("how many fibbonaccis do y'all need:  "))

a = 0
b = 1

for i in range(1, x + 1):
    c = a + b
    a = b
    b = c
    print(c)