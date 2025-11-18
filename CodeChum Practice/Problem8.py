# Write a program that analyzes a string character by character until it encounters a period (.) or reaches the end.
# Count uppercase letters, lowercase letters, digits, and spaces. Skip special characters (don't count them).

word = input()
caseUpper = 0
caseLower = 0
space = 0
num = 0
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #lmao

for i in range((len(word)-1), -1, -1):
    if len(word) > 200:
        break
    elif word[i] in letters:
        caseUpper+= 1
    elif word[i] in letters.lower(): #lmaoooo
        caseLower+= 1
    elif word[i] in " ":
        space+= 1
    elif word[i] in "0123456789":
        num+= 1

print("Uppercase:", caseUpper)
print("Lowercase:", caseLower)
print("Digits:", num)
print("Spaces:", space)