with open('countries.txt', 'r') as file:
    for line in file:
        print(line, end="")
    file.close()
    