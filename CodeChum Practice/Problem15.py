# Write a program that reads n student grades and categorizes them into grade brackets:
# A (90-100), B (80-89), C (70-79), D (60-69), F (below 60). Display how many students fall into each category.

A = B = C = D = F = 0
n = int(input())
grades = input()
grades = [int(x) for x in grades.split()]

for i in range (n):
    if 100 >= grades[i] > 89:
        A += 1
    elif 89 >= grades[i] > 79:
        B += 1
    elif 79 >= grades[i] > 69:
        C += 1
    elif 69 >= grades[i] > 59:
        D += 1
    elif 59 >= grades[i]:
        F += 1
    else:
        continue

print("A:", A)
print("B:", B)
print("C:", C)
print("D:", D)
print("F:", F)