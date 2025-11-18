# Checksum Validator

check = input("Enter string: ")
key = int(input("Enter key: "))
checksum = 0
letters = []
numbers = []
i = -1

for x in check:
    if x.isupper():
        letters.append(x)
        i += 1
        numbers.append("")
    elif x.isdigit():
        numbers[i] = numbers[i] + x

for j in range (len(letters)):
    checksum += ord(letters[j]) * int(numbers[j])

if (checksum % key) == 0:
    print("Result: Valid")
else:
    print("Result: Corrupt")