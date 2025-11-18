# Create a simple student record system that stores names and three test scores for n students. Calculate and display each student's average and overall class average.

n = int(input())
array =[]
classTotal = 0

for i in range (n):
    a = []
    sum = 0
    column = input()
    column = column.split()
    a.append(column[0])
    for j in range (1, 4):
        sum += int(column[j])
    a.append(sum / 3)
    array.append(a)

print()

for i in range (n):
    print(f"{array[i][0]}: {array[i][1]:.2f}")
    classTotal += array[i][1]

classAverage = classTotal / n
print(f"Class average: {classAverage:.2f}")