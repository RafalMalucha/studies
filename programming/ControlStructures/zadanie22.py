for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} BINGO")
    elif i % 5 == 0:
        print("FIVE")
    elif i % 3 == 0:
        print("THREE")
    else:
        print(i)