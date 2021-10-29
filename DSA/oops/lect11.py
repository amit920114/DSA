
class Student:

    name = "Amit"

    def details(self):
        self.firstName = "Amit"
        self.lastName = "Kumar"

    def marks(self):
        print("My name is ", self.firstName,
              self.lastName, "and i am in 10 Standard")

    @staticmethod
    def stMethod():
        print("I am Static Method inside the Class Student")
        return ""


s1 = Student()
print(s1.name)
s1.details()
print(s1.marks())
print(s1.stMethod())
