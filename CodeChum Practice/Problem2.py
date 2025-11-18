# Write a program that prints a number pyramid pattern based on user input. The pattern should have n rows where n is provided by the user

size = int(input())

for i in range(1, size+1):
    for j in range(1, i+1):
        print(j, end="")
    print()