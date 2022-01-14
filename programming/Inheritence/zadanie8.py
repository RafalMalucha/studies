import time

class phone():
    
    def __init__(self, make, model, version):
        self.make = make
        self.model = model
        self.active = False
        self.os = version
        
    def __str__(self):
        return(f"make: {self.make} \n"
               f"model: {self.model} \n"
               f"android version: {self.os}")
        
    def phone_on(self):
        self.active = True
    
    def phone_off(self):
        self.active = False
    
    def update_os(self, version):
        self.os = version
        print("Downloading...0%")
        time.sleep(1)
        print("Downloading...10%")
        time.sleep(0.5)
        print("Downloading...50%")
        time.sleep(0.3)
        print("Downloading...75%")
        time.sleep(0.7)
        print("Downloading...99%")
        time.sleep(3)
        print("Downloading...100%")
        print("Installing...0%")
        time.sleep(0.3)
        print("Installing...10%")
        time.sleep(0.6)
        print("Installing...11%")
        time.sleep(0.1)
        print("Installing...12%")
        time.sleep(0.1)
        print("Installing...13%")
        time.sleep(0.1)
        print("Installing...66%")
        time.sleep(0.5)
        print("Installing...99%")
        time.sleep(0.2)
        print("Installing...100%")
        time.sleep(0.1)
        print("Done")
        print("OS updated")
        
    
    def behavior1(self):
        pass
    
    def behavior2(self):
        pass
    
phone1 = phone("apple", "iPhone 15,5", "2115")
phone2 = phone("krzak", "dwa krzaki", "2137")
print(phone1)
phone1.update_os("9.9")
print(phone1)

