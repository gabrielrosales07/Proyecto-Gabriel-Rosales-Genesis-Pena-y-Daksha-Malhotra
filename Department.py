class Department:
    def __init__ (self, id, name):
        self.id = id
        self.name = name

    def show (self):
        print (f"Id: {self.id}")
        print (f"Name: {self.name}")
