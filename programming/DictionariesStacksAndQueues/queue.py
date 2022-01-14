queue = []
def push(value):
    queue.append(value)
    
def pull():
    queue.pop()
    
def display():
    for i in queue:
        print(i, end=" ")
    print()
