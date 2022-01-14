import stack

number = int(input("Number: "))

for i in range(8):
    x = number % 2
    number = number // 2
    stack.push(x)
    if number == 0:
        break

binary = ""

for i in range(8):
    binary += str(stack.pop())
    if stack.empty() == True:
        break
    
print(f"Number but in binary: {binary}")



