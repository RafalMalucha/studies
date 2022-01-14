class student():
    
    ID = 100000
    
    def __init__(self, name, surname, study):
        student.ID += 1
        self.id = student.ID
        self.name = name
        self.surname = surname
        self.study = study
    
    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Surname: {self.surname}\n"
                f"ID: {self.id}\n"
                f"Study: {self.study}")
    
one = student("kurwa", "chuj", "dupa")
dos = student("szczyny", "gówno", "rzygi")
print(one)
print(dos)
    