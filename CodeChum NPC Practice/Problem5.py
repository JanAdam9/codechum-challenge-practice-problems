# Minimal Cyclic Shift

s = input("Enter string: ")
cycles = []

for i in range (len(s)):
    s = s[1:] + s[:1]
    cycles.append(s)

cycles.sort()
print("Result:", cycles[0])