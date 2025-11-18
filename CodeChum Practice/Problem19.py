# Write a program that checks if a given string is a palindrome (reads the same forwards and backwards). Ignore spaces and case.

word = input()
word = word.replace(" ","").lower()

reverse = ""

for i in range (len(word)-1, -1, -1):
    reverse += word[i]

if word == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")