# Exceptions and Errors
x = -5
# if x < 0:
#     raise Exception(f"{x} is smaller than 0 ")

# assert(x < 0), " is smaller than Zero "
# # print(x)

# Try and Except Method

try:
    a = 5 % 0
except:
    print("Error Occured")

print("*"*50)
print("*"*50)

try:
    c = 4 % 0
except Exception as w:
    print(w)

print("*"*50)
print("*"*50)
print("*"*50)
try:
    # gh = 12 % 0
    g = 12 + "20"
    m = 12+20
except ZeroDivisionError as v:
    print(v)
except TypeError as t:
    print(t)

else:
    print("Every thing is Correct")

finally:
    print("Looks GOOD")
print("*"*50)

# Maje your own Error
# Custom ERRORS


class VALUETOOHIGH(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_val(x):
    if x > 100:
        raise VALUETOOHIGH("value is too high ", x)


try:
    test_val(500)
except VALUETOOHIGH as e:
    print(e)
