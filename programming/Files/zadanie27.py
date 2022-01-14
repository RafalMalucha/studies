import re

with open("lorem.txt", "r") as file:
    words_6orMore = re.findall("\w+{6,}", "lorem.txt")
    
print(words_6orMore)



#print(f"Threre are {len(words_6orMore)} in this text")