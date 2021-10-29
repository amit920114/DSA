# Sallow Vs Deep Copying


import copy


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Company:
    def __init__(self, boss, employee):
        self.Boss = boss
        self.Employee = employee


p1 = Person("Amit", 22)
p2 = Person("Shahil", 20)

company = Company(p1, p2)
company_clone = copy.deepcopy(company)
company_clone.Boss.age = 56
print("company")
print(company.Boss.age)

print("company_clone")
print(company_clone.Boss.age)
