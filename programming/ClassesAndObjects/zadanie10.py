class TVset():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        
    def turn_on(self):
        self.is_on = True
        
    def turn_off(self):
        self.is_on = False
        
    def set_channel(self, num):
        self.channel_no = num
        
    def show_status(self):
        if self.is_on:
            print(f"TV is on, channel number {self.channel_no}")
        else:
            print("TV is off")
            
tv = TVset()
tv.show_status()
tv.turn_on()
tv.show_status()
tv.set_channel(55)
tv.show_status()
tv.turn_off()
tv.show_status()
