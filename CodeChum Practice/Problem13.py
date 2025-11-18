# Write a program that takes two strings and performs various string operations: concatenation, length comparison, and alphabetical comparison.

word1 = input()
word2 = input()
wordList = [word1, word2]
wordList.sort()

print("Concatenated:", word1+word2)
if len(word1) < len(word2):
    print(word1, "is shorter")
elif len(word1) > len(word2):
    print(word2, "is shorter")
else:
    print("Both are of equal length")
print(wordList[0], "comes first alphabetically")