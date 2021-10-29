# Check if List is Sorted or Not
print("Check if List id Sorted or Not:--")


def func(list):
    # l = len(list)
    if len(list) == 0 or len(list) == 1:
        return True
    if list[0] > list[1]:
        return False
    smallList = list[1:]
    # smallList = list[]
    isSmallList = func(smallList)
    return isSmallList


# n = int(input("Enter the number:-- "))
list = [1, 2, 3, 4]
kk = func(list)
print(kk)
