# AbsTract Classes
from abc import ABC, abstractmethod


class AutoMobile(ABC):
    def __init__(self, Wheels):
        self.Wheels = Wheels
        return print("AutoMobile Created")

    @abstractmethod
    def start(self):
        print("My name is Khan")

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def getWheels(self):
        return self.Wheels


class Car(AutoMobile):
    # def __init__(self, Wheels):
    #     super().start(Wheels)
    #     print("Car Created")

    def start(self):
        print("My name is Khan")

    def stop(self):
        pass

    def drive(self):
        pass

    def getWheels(self):
        return self.Wheels

    def __str__(self) -> str:
        return "Ureka! Ureka!"


# -----------Note--------
# k = AutoMobile()  # We can not Create a Object Using abstractMethods
# print(k)
# And The child class must have abstract methos in them
# Otherwise :- Can't instantiate abstract class,
#  AutoMobile with abstract methods
# Error Will Occurs
c = Car(18)
# c.getWheels(4)
print(c.getWheels())
print(c.start())
print(c)
