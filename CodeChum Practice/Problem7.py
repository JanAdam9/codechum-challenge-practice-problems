# Write a program that reads two matrices (2D arrays) of the same dimensions and computes their sum.

size = input()
size = [int(x) for x in size.split()]

matrix1 = []
matrix2 = []
matrix3 = []

for i in range(size[0]):
    a = []
    column = input()
    column = column.split()
    for j in range(size[1]):
        a.append(int(column[j]))
    matrix1.append(a)

for i in range(size[0]):
    a = []
    column = input()
    column = column.split()
    for j in range(size[1]):
        a.append(int(column[j]))
    matrix2.append(a)

for i in range(size[0]):
    a= []
    for j in range(size[1]):
        a.append(matrix1[i][j] + matrix2[i][j])
    matrix3.append(a)

for i in range (size[0]):
    for j in range(size[1]):
        print(matrix3[i][j], end=" ")
    print()