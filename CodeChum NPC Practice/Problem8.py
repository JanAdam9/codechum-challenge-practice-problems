# Recursive Cipher Decoder

reference = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
cipher = input("Enter string: ")

def Decode(x):
    i = 0
    newString = ""
    while i < len(x):
        if i >= len(x)-1:
            newString += x[i]
            break
        elif x[i+1].isdecimal():
            oldVal = reference.index(x[i])
            newVal = (int(oldVal) - int(x[i+1]) + 36) % 36
            newString += reference[newVal]
            i += 1
        else:
            newString += x[i]
        i += 1
    return newString

def NoDecimal(y):
    check = True
    for i in range (1, len(y)):
        if str(y[i]).isdecimal():
            check = False
            break
    return check

while True:
    if NoDecimal(cipher):
        break
    prev = cipher
    cipher = Decode(cipher)
    if len(cipher) <= 1:
        break
    if prev == cipher:
        break
    
print("Result:",cipher)