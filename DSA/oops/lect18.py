# Addition Sybstraction and other functions
# Will Do it Later


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        # return "This point "
        pass

    def __add__(self, point_obj):
        return Point(self.__x + point_obj.__x, self.__y + point_obj.__y)


p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3)
