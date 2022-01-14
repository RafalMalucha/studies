file = open("powers.txt", "w")
for i in range(1,11):
    string = str(i) + ", " + str(i ** 2) + ", " + str(i ** 3) + "\n"
    file.write(string)
    
file.close()