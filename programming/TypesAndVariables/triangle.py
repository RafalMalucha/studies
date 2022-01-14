a = float(input("bok 1: "))
b = float(input("bok 2: "))
c = float(input("bok 3: "))

z = (a + b + c)/2

p = (z*(z - a)*(z - b)*(z - c))**(1/2)

if a + b < c:
    print("prosze przypomniec sobie wlasnosci trojkata")
elif c + a < b:
    print("prosze przypomniec sobie wlasnosci trojkata")
elif b + c < a:
    print("prosze przypomniec sobie wlasnosci trojkata")
else:
    print(f"pole trojkata = {p}")
    
input("Press enter to exit ;)")