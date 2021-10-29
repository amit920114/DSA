# PolymorPhism:- Method Overriding
# The method of chid is oVerride the method of Parent's Class


class Vehicle:
    def __init__(self, color, maxSpeed):
        self.Color = color
        self.__maxSpeed = maxSpeed

    def __str__(self):
        return (
            "(This is Vehicle(parent) ClS and Takes color and maxSpeed as an argument)"
        )

    def getMaxSpeed(self):
        return self.__maxSpeed

    def setMaxSpeed(self, maxSpeed):
        self.__maxSpeed = maxSpeed

    def printFunc(self):
        print("Color :", self.Color)
        print("maxSpeed :", self.__maxSpeed)


class Car(Vehicle):
    def __init__(self, color, maxSpeed, numGears, isConvertivle):
        super().__init__(color, maxSpeed)
        self.numGers = numGears
        self.isConvertuble = isConvertivle

    def __str__(self):
        super().__str__()
        return "This is Car(child) class overides the parents Class "

    def printFunc(self):
        # self.printFunc()  --Check This Too--
        # This will cause
        # recursion Problem
        # as this will
        # keep calling itself again and
        #  again
        super().printFunc()  # To get rid of
        #  recursion we user
        #  super() method to inherits the properties
        print("numbersGears :", self.numGers)
        print("is Convertible :", self.isConvertuble)


c = Car("Red", 45, 6, True)
c.printFunc()
print(c)  # By Default This Will gives
# This as a O/p -> <__main__.Car object at 0x0000028DF25BCFA0>
# But If We Set via method __str__ (Used for custom description)
