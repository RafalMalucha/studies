class bruh():
    
    @staticmethod
    def circle(radius):
        area = 3.14 * (radius ** 2)
        print(area)
    
    @staticmethod
    def rectangle(side1, side2):
        area = side1 * side2
        print(area)
    
    @staticmethod
    def triangle(base, height):
        area = 0.5 * base * height
        print(area)
    
side1 = 5
side2 = 16 
radius = 33
base = 55
height = 4 
bruh.circle(radius)
bruh.rectangle(side1, side2)
bruh.triangle(base, height)
