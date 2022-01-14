class TVset():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.volume = 0
        
    def turn_on(self):
        self.is_on = True
        
    def turn_off(self):
        self.is_on = False
        
    def set_channel(self, num):
        self.channel_no = num
        
    def show_status(self):
        if self.is_on:
            print(f"TV is on, channel {self.channel_no}, volume {self.volume}")
        else:
            print("TV is off")
            
    def vol_up(self):
        if self.is_on:
            if self.volume == 10:
                pass
            else:
                self.volume += 1
        else:
            pass
        
    def vol_down(self):
        if self.is_on:
            if self.volume == 0:
                pass
            else:
                self.volume -= 1
        else:
            pass
        
        
tv = TVset()
tv.show_status()
tv.turn_on()
for i in range(2):
    tv.vol_up()
tv.show_status()
tv.set_channel(55)
tv.vol_down()
tv.show_status()
tv.turn_off()
tv.show_status()