
file = open("lorem.txt", 'r')
line_count = 0
for line in file:
    print(line, end="")
    line_count += 1
    if line_count % 5 == 0:
        enter = input()
        if enter == "":
            continue
            
            
file.close()