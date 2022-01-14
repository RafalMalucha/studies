import random

class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
    
    @staticmethod
    def same_value_array(number_of_array_elements, value_of_array_elements):
        bruh = []
        for i in range(number_of_array_elements):
            bruh.append(value_of_array_elements)
        print(bruh)
        
    @staticmethod
    def random(number_of_array_elements, value_from, value_to):
        breeh = []
        for i in range(number_of_array_elements):
            breeh.append(random.randint(value_from, value_to))
        print(breeh)
        
    @staticmethod
    def inRange(array, value_from, value_to):
        amount = 0
        for c in range(len(array)):
            if array[c] >= value_from and array[c] <= value_to:
                amount += 1
            else:
                pass
        print(amount)
        
            
my_array = [4,1,8,7,2]
#Arrays.print_in_col(my_array)
#Arrays.random(10, 1, 15)
Arrays.inRange(my_array, 7,8)

