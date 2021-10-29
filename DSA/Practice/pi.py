# Replace pi with 3.14


def removepi(str):
    l = len(str)
    if l == 0 or l == 1:
        return str
    if str[0] == "p" and str[1] == "i":
        return "3.14" + removepi(str[2:])
    return str[0] + removepi(str[1:])


# op = "piklpi"
# print(removepi(op))
# Remove Duplicates


def removeDup(str):
    l = len(str)
    if l == 0 or l == 1:
        return str
    if str[0] == str[1]:
        return str[0] + removeDup(str[2:])
    else:
        return str[0] + removeDup(str[1:])


kk = "mmkkllllkmm"
print(removeDup(kk))
