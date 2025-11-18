# Balanced Rotation Index

size = int(input("Enter array size: "))
print("Enter the elements:")
ar = input()
arr = list(map(int, ar.split()))

def ArraySum(a):
    total = 0
    for i in range (size):
        total += i*a[i]
    return total
    
sumList = [ArraySum(arr)]

for i in range (size - 1):
    arr.append(arr.pop(0))
    sumList.append(ArraySum(arr))
    
print("Balanced Rotation Index:", sumList.index(min(sumList)))