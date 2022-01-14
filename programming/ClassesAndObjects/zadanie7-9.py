class University():

    # object constructor (__init__ method)
    def __init__(self, name, fullname):
        # object states/attributes (fields)
        self.name = name
        self.fullname = fullname

    # object bahaviors (methods)
    def print_name(self):  
        print(self.name)
    def set_name(self, name):
        self.name = name
    def print_fullname(self):
        print(self.fullname)
    def set_fullname(self, fullname):
        self.fullname = fullname
    


uni1 = University('uek', "uniwersytet ekonomiczny w krakowie")
uni1.print_name()
uni1.print_fullname()
uni1.set_name('agp')
uni1.set_fullname('akademia gurniczo pierdnicza')
uni1.print_name()
uni1.print_fullname()