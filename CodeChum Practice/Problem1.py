# Write a program that calculates a student's final grade based on three exam scores.
# The program should compute the average and display whether the student passed or failed. A passing grade is 75 or above.

grade1 = int(input())
grade2 = int(input())
grade3 = int(input())

average = round((grade1+grade2+grade3)/3, 2)
print("Average:",average)
if average > 75:
    print("Result: Passed")
else:
    print("Result: Failed")