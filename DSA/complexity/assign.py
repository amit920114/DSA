# Time And Space Complexity
# print("Hey! Amit Kumar")
# print("Welcome to Learn Time and Space Complexity")

# X to Power n Using Recurssion


def power(x, n):
    if n == 0:
        return 1

    op = x * power(x, n - 1)
    return op


# Time Complexity is O(n)
# Space Complexity is O(n)
# -----------OUTPUT----------------
# op = power(2, 5)
# print(op)


def pow(x, n):
    i = 0
    ans = 1

    while i < n:
        ans = ans * x
        i += 1
    # Time Complexity O(1)
    # Space Complexity O(1)
    return ans


# -----------OUTPUT----------------
# op2 = pow(2, 4)
# print(op2)

# Recursive Approch but better way to
# Space and Time Complexity


def power2(x, n):
    if n == 0:
        return 1

    smallOp = power2(x, n // 2)

    if n % 2 == 0:
        return smallOp * smallOp

    else:
        return smallOp * smallOp * x


# Now The Time and Space complexity is O(logn)

# -----------OUTPUT----------------
k = power2(2, 5)
print(k)
