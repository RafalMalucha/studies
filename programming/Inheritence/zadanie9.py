class book():
    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = year
        
class ebook(book):
    def __init__(self, file, author, title, year):
        super().__init__(author, title, year)
        self.file = file
    def __str__(self):
        return (f'author: {self.author}\n'
                f'title: {self.title}\n'
                f'year: {self.year}\n'
                f'file: {self.file}')
        
class paper(book):
    def __init__(self, pages, author, title, year):
        super().__init__(author, title, year)
        self.pages = pages
    def __str__(self):
        return (f'author: {self.author}\n'
                f'title: {self.title}\n'
                f'year: {self.year}\n'
                f'pages: {self.pages}')
    
boek = paper(51235, "asd", "asfa", "123")
boook = ebook("bruh.jpg", "aaa", "asd", "2137")
print(boek)
print(boook)
        
    