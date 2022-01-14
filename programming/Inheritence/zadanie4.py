class song():
    
    def __init__(self, artist, song, album, year):
        self.artist = artist
        self.song = song
        self.album = album
        self.year = year
        
    
    def __str__(self):
        return(f"Performer: {self.artist} \n"
               f"Song: {self.song} \n"
               f"Album: {self.album} \n"
               f"Year: {self.year} \n")
    
x = song("asda", "asdasf", 'gags', 'gadhe')

print(x)
