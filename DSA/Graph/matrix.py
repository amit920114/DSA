# Matrix Array
R = int(input("Enter number of rows:"))
C = int(input("Enter number of Columns:"))
matrix = []
for i in range(R):
    print("Enter Data rows wise")
    a = []
    for k in range(C):
        val = int(input())
        a.append(val)
    matrix.append(a)

for i in range(R):
    for k in range(C):
        print(matrix[i][k], end=" ")
    print()
