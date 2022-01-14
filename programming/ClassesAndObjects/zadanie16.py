class Book():
    
    def __init__(self):
        self.is_open = False
        self.author = "Adrian Newey"
        self.title = "How to Build a Car: The Autobiography of the World’s Greatest Formula 1 Designer"
        self.pages_amount = 330
        self.current_page = 0
        
    def book_open(self):
        self.is_open = True
        
    def book_close(self):
        self.is_open = False
        
    def next_page(self):
        if self.is_open:
            if self.current_page == 330:
                pass
            else:
                self.current_page += 1
        else:
            pass
            
    def previous_page(self):
        if self.is_open:
            if self.current_page == 0:
                pass
            else:
                self.current_page -= 1
                
    def print_title(self):
        print(self.title)
        
    def print_author(self):
        print(self.author)
        
    def status(self):
        if self.is_open:
            print(f"{self.title}, by {self.author}, number of pages: {self.pages_amount}, current page: {self.current_page}")
        else:
            print(f"{self.title}, by {self.author}, number of pages: {self.pages_amount}, currently closed")
            

    
    