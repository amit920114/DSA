# Check if the number is balanced:


def isBalance(str):
    n = len(str)
    mid = n // 2
    for i in range(0, n):
        sum1 = 0
        sum2 = 0
        for k in range(0, mid):
            sum1 = sum1 + int(str[k])
        for j in range(mid + 1, n):
            sum2 = sum2 + int(str[j])
        if sum1 == sum2:
            return True
        else:
            return False
    # return sum1, sum2


str = "1234006"
print(isBalance(str))
