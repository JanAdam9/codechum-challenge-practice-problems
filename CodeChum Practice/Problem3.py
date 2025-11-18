# Write a program that takes a string input, reverses it, and counts the number of vowels (a, e, i, o, u - case insensitive) in the original string.

word = input()
vowel = 0

print("Reversed: ", end="")

for i in range((len(word)-1), -1, -1):
    print(word[i], end="")
    if word[i] in "aeiou":
        vowel+= 1
        
print("\nVowels:", vowel)