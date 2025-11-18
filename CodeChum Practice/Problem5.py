# Write a program that reads n integers into an array and calculates the sum, average, maximum, and minimum values.

n = int(input())
array = input()
sum = 0

intArray = [int(x) for x in array.split()]
intArray.sort()

for i in intArray:
    sum += i

average = sum/n

print("Sum:", sum)
print(f"Average: {average:.2f}")
print("Maximum:", intArray[n-1])
print("Minumum:", intArray[0])