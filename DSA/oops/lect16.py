from datetime import date


class Student:
    def __init__(self, name, age, per):
        self.__name = name
        self.age = age
        self.persentage = per

    @classmethod
    def fromBirth(Cls, name, year, per):
        Cls(name, date.today().year - year, per)
        print(name, date.today().year - year, per)


k = Student("Amit", 22, 95)
# s = Student.fromBirth("Papa", 1975, 99)
# print(k.__name) canNot get acces as these are private variable
# But in python there is no Concept of private variables so we can get access to those variables too
# by following the method obj._Classname__variablename
print(k._Student__name)  # accesed to private Variable
