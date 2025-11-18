# Write a program that calculates the power of a number using both a loop and the built-in power function. Display both results and verify they match.

import math

num = int(input())
exp = int(input())

loop = 1
meth = math.pow(num, exp)

for i in range (exp):
    loop *= num

print("Loop result:", loop)
print("Math function result:", meth)

if loop == meth:
    print("Match")
else:
    print("No match")