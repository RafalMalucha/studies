file = open("lorem.txt", "r")
file_copy = open("copy.txt", "w")

file_content = file.read()

file_copy.write(file_content)

file.close()
file_copy.close()