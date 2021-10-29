# Decorators are very useful in python as it runs functions inside another function
# @decorators
import functools


def start_end(func):
    def wrapper():
        print("START")
        func()
        print("END")
    return wrapper


def print_name():
    print("Amit")


print_name()
print("*"*50)
print("*"*50)


@start_end
def printing_name():
    print("Amit Kumar")


printing_name()
print("*"*50)


def my_name(funtn):

    def wrap():
        print("My Name")
        funtn()
        print("kumar")
    return wrap


@my_name
def is_amit():
    print("IS AMIT")


print("*"*50)
print("*"*50)
is_amit()

# Functions argument
print("*"*50)
print("*"*50)


def addition(func):
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper


@addition
def add10(num):
    return num + 10


val = add10(45)
print(val)
print(add10.__name__)
print("*"*50)
print("*"*50)
# functools


def addition(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper


@addition
def add10(num):
    return num + 10


val = add10(45)
print(val)
print(add10.__name__)
# print(help(add10))


def repeat(num_times):
    def deco_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("Start")

            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return deco_repeat


@repeat(2)
def greet(name):
    print(f"hello{name}")


greet("Amit")

# Decorators in Class


# class countcalls():
#     def __init__(self, func):
#         functools.update_wrapper(self, func)
#         self.func = func
#         self.num_calls = 0


# def __call__(self, *args, **kwargs):
#     self.num_calls += 1
#     print(f"call {self.num_calls} of {self.func.__name__!r}")
#     return self.func(*args, **kwargs)


# @countcalls
# def say_hello(num):
#     print("hello")


# say_hello(5)


class CountCalls:
    # the init needs to have the func as argument and stores it
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    # extend functionality, execute function, and return the result
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello(num):
    print("Hello!")


say_hello(5)
# say_hello(5)

print("*"*50)
print("*"*50)

print("Class Decorators")
print("*"*50)
print("*"*50)


class countCalls:

    def __init__(self, func):
        self.func = func
        self.num_times = 0

    def __call__(self, *args, **kwds):
        self.num_times += 1
        print(f"this is executes {self.num_times} times")
        return self.func(*args, **kwds)


@countCalls
def say_Hey():
    print("Hi My name is Amit Kumar")
    return ""


j = say_Hey()
print(j)
