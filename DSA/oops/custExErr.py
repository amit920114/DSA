# ---------DO READ COMMENTS----------#

# Custom Execption errors handling :-


# class ZeroDenominatorError(Exception):
#     pass


class ZeroDenominatorError(ZeroDivisionError):
    pass


while True:
    try:
        num = int(input("Enter the numerator: - "))
        demon = int(input("Enter the Denominator: - "))
        if demon == 0:
            raise ZeroDenominatorError("Denominator must be greator than 0")
        value = num / demon

    except ValueError:
        print("Value error is raised")
    except ZeroDivisionError:
        print("Zero Division error has been Raised")
    except ZeroDenominatorError:
        print("Denominator Zero Error Has been Raised")
    else:
        print(value)
        break
    finally:
        print(num)
        print(demon)
        print(value)
        print("Exception and Errors are Done Now")
