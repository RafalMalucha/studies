a = int(input("szerokosc:  "))

b = int(input("wysokosc  "))

for x in range(a, (a + 1)):
    print(f"*" * x)
    for y in range(1, (b - 1)):
        print("*", " " * (a - 4), "*")
    print(f"*" * x)





