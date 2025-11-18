# Write a program that demonstrates all assignment operators. Start with an initial value and perform a series of operations using compound assignment operators.

leList = []
n = int(input())
n += int(input())
leList.append(n)
n -= int(input())
leList.append(n)
n *= int(input())
leList.append(n)
n /= int(input())
leList.append(n)
n %= int(input())
leList.append(n)

print("After +=:", leList[0])
print("After -=:", leList[1])
print("After *=:", leList[2])
print("After /=:", int(leList[3]))
print("After %=:", int(leList[4]))