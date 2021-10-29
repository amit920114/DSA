# Error Handling And Exceptions

while True:
    try:
        num = int(input("Enter the numberator:- "))
        denom = int(input("enter the denominator:- "))
        OutPut = num / denom
        print(OutPut)
        break
    except ValueError:
        print("Numerator and denominator must be an Integer")
