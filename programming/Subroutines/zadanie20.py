def power(x, n):
    y = x ** n
    y = x * (x ** (n -1))
    return y
    
    
print(power(5,3))