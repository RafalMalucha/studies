file = open('countries.txt', 'r')
line_count = 0
for line in file:
    line_count += 1
print(f"There are {line_count} lines in {file.name}")
file.close()