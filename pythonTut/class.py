
# def __init__(self,fname,lname)

class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname

    def myfunc(self):
        print(self.firstName + self.lastName)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.Year = year

    def Welcome(self):
        print("Welcome", self.firstName, self.lastName, self.Year, "Batch")


# z = Student("Amit", "Kumar", 2022)
# print(z.Year)
# v = Person("Ajay ", "Khandelwal")
# print(v.myfunc())
d = Student("Amit", "Kumar", 2018)
print(d.Welcome())
