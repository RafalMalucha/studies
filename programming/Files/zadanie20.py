file = open("ints50.txt", "w")
for i in range(1,51):
    string = str(i) + "\n"
    file.write(string)
    
file.close()