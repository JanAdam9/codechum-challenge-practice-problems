# Generate the first n numbers of the Fibonacci sequence and store them in an array. Display the sequence and the sum of all numbers.

n = int(input())
sum = 0
sequence = [0, 1]

for i in range (1,n-1):
    sequence.append(sequence[i]+sequence[i-1])
    
for i in range (n):
    sum += sequence[i]

print("Sequence:", end=" ")
for i in range (n):
    print(sequence[i], end=" ")

print()
print("Sum:", sum)