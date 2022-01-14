def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

class stats():
    
    def __init__(self):
        self.array = []
        
    def add(self, num):
        self.array.append(num)
        
    def delete(self, num):
        to_del = 0
        for i in range(len(self.array)):
            if self.array[i] == num:
                to_del += i
        self.array.pop(to_del)
        
    def disp(self):
        string = ''
        for i in range(len(self.array)):
            string += str(self.array[i]) + " "
        print(string)
        
    def greatest(self):
        bubblesort(self.array)
        print(self.array[len(self.array) - 1])
        
    def smallest(self):
        bubblesort(self.array)
        print(self.array[0])
        
    def median(self):
        bubblesort(self.array)
        if len(self.array) % 2 == 0:
            print((self.array[(len(self.array) // 2)] + self.array[(len(self.array) // 2) - 1]) / 2)
        if len(self.array) % 2 != 0:
            print(self.array[(len(self.array) // 2)])
            
    def mean(self):
        summ = 0
        for i in range(len(self.array)):
            summ += self.array[i]
        mean = summ / len(self.array)
        print(mean)
        
bbb = stats()
bbb.disp()
bbb.smallest()
bbb.disp()
bbb.mean()
bbb.median()
bbb.delete(2)
bbb.disp()

