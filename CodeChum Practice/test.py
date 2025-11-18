reference = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
cipher = "999"

def Decode(x):
    i = 0
    newString = ""
    while i < len(x):
        if x[i+1].isdecimal():
            oldVal = reference.index(x[i])
            newVal = (int(oldVal) - int(x[i+1]) + 36) % 36
            newString += reference[newVal]
            i += 1
        else:
            newString += x[i]
        i += 1
    return newString

print(Decode(cipher))