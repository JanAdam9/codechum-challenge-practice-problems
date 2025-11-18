# Word Shape Counter

words = input("Enter a string: ")
upper = lower = digit = symbol = 0


for x in words:
    if x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        upper += 1
    elif x in "abcdefghijklmnopqrstuvwxyz":
        lower += 1
    elif x in "0123456789":
        digit += 1
    else:
        symbol += 1
        
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
print("Digits:", digit)
print("Symbols:", symbol)