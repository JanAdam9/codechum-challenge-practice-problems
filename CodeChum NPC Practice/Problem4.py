# Largest Prime Gap

size = int(input("Enter array size: "))
ar = input("Enter the numbers: ")
arr = list(map(int, ar.split()))
primeList = []

def PrimeCheck(num):
    check = True
    for i in range(2, num, 1):
        if (num % i) == 0:
            check = False
            break
    return check

for i in range (size):
    if PrimeCheck(arr[i]):
        primeList.append(arr[i])

if len(primeList) > 1:
    primeList.sort()
    differenceList = []
    for i in range (len(primeList)-1):
        differenceList.append(primeList[i+1] - primeList[i])
    
    posLargest = differenceList.index(max(differenceList))

    print(f"Largest gap is: {max(differenceList)} between primes {primeList[posLargest]} and {primeList[posLargest+1]}")
    
else:
    print("Not enough primes to form a gap.")