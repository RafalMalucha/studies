import random

class Thermo():
    
    def __init__(self):
        self.is_on = False
        self.temp = 0
        
    def Thermo_on(self):
        self.is_on = True
        
    def Thermo_off(self):
        self.is_on = False
        
    def Thermo_measure(self):
        if self.is_on:
            x = random.uniform(34.0, 42.0)
            temperature = "%.1f" % x
            self.temp = temperature
        else:
            pass
        
    def Thermo_read(self):
        if self.is_on:
            if float(self.temp) > 37 and float(self.temp) < 41:
                print(f"temperature: {self.temp} (fever)")
            elif float(self.temp) > 41:
                print(f"temperature: {self.temp} (CRITICAL TEMPERATURE!!)")
            elif self.temp == 0:
                print("you got to measure temperature first")
            else:
                print(f"temperature: {self.temp}")
        else:
            print("thermometer is off")
            
t = Thermo()
t.Thermo_read()
t.Thermo_on()
t.Thermo_read()
for i in range(15):
    t.Thermo_measure()
    t.Thermo_read()
t.Thermo_off()
t.Thermo_read()
    
    
    
    
    
    
    
    
    
    