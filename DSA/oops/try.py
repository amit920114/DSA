class Student:
    def __init__(self, name, roll):
        self.name = name
        self.rollNumber = roll

    def print_op(self):
        print(self.name)
        print(self.rollNumber)


s = Student("Naman", 478)
s.print_op()
