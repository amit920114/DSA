# Multiple inheritance


class Father:
    def __init__(self):
        self.Name = "Virat"
        super().__init__()


class Mother:
    def __init__(self):
        self.Name = "Anuska"


class Child(Father, Mother):
    def __init__(self):
        super().__init__()

    def printFunc(self):
        print("Name is", self.Name)


c = Child()
c.printFunc()
print(Child.mro())
