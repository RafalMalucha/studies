x = int(input("podaj współrzędną x punktu:  "))
y = int(input("podaj współrzędną y punktu:  "))

if x > 0 and y > 0:
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"Point P({x}, {y}) is in the first quadrant of the coordinate system")
elif x > 0 and y < 0:
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"Point P({x}, {y}) is in the second quadrant of the coordinate system")
elif x < 0 and y < 0:
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"Point P({x}, {y}) is in the third quadrant of the coordinate system")
elif x < 0 and y > 0:
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"Point P({x}, {y}) is in the fourth quadrant of the coordinate system")
else:
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"Point P({x}, {y}) is directly on the axis")