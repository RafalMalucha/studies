names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest = 0

for i in range(len(names)):
    if len(names[i]) > len(names[longest]):
        longest = i
    else:
        continue
    
print(names[longest])