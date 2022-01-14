import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C"
temperatures = re.findall("\d{2}", message)

summ = 0

for i in range(0, len(temperatures)):
    summ += int(temperatures[i])
    
mean = summ / len(temperatures)

print(mean)