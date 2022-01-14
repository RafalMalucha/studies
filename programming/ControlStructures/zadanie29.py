a = int(input("Enter number:  "))
quan = 0
summ = a

while a != 0:
    a = int(input("Enter number:  "))
    quan += 1
    summ += a
    
    if a == 0:
        mean = summ / quan 
        print(f"RESULT: Quantity={quan}, Sum={summ}, Mean={mean}")
    
    

    


