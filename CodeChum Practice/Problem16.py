# Write a program that reads a matrix and displays its transpose (rows become columns and vice versa).

n = input()
n = [int(x) for x in n.split()]
array = []
transpose = []
print()

for i in range (n[0]):
    a = []
    column = input()
    column = [int(x) for x in column.split()]
    for j in range (n[1]):
        a.append(column[j])
    array.append(a)

for i in range (n[1]):
    b = []
    for j in range (n[0]):
        b.append(array[j][i])
    transpose.append(b)

print()

for i in range (n[1]):
    for j in range(n[0]):
        print(transpose[i][j], end=" ")
    print()