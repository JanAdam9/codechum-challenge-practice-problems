# Write a program that reads two matrices (2D arrays) of the same dimensions and computes their sum.

size = int(input())
grandTotal = 0
matrix = [["ITEM", "QTY", "PRICE", "TOTAL"]]

for i in range(size):
    a = []
    column = input()
    column = column.split()
    a.append(column[0])
    a.append(int(column[1]))
    a.append(float(column[2]))
    total = a[1] * a[2]
    a.append(total)
    grandTotal += total
    matrix.append(a)
print()

for i in range (4):
    print(matrix[0][i], end="\t")
print()

for i in range (1,size+1):
    print(matrix[i][0], end="\t")
    print(matrix[i][1], end="\t")
    print(f"{matrix[i][2]:.2f}", end="\t")
    print(f"{matrix[i][3]:.2f}", end="\t")
    print()

print("--------------------------------")
print(f"GRAND TOTAL:\t\t{grandTotal:.2f}")