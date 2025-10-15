# CodeChum NPC 2025 Practice Problems - Complete Set (20 Problems)

## Problem 1: Student Grade Calculator
**Topics:** Input operations, Arithmetic operators, Output operations, Selection structures (if-else)

**Problem Description:**
Write a program that calculates a student's final grade based on three exam scores. The program should compute the average and display whether the student passed or failed. A passing grade is 75 or above.

**Input:**
- Three integer scores (0-100)

**Output:**
- The average (with 2 decimal places)
- "Passed" if average >= 75, otherwise "Failed"

**Sample Input:**
```
85
90
78
```

**Sample Output:**
```
Average: 84.33
Result: Passed
```

---

## Problem 2: Pattern Printer with Loops
**Topics:** Iterative structures (nested loops), Output operations

**Problem Description:**
Write a program that prints a number pyramid pattern based on user input. The pattern should have n rows where n is provided by the user.

**Input:**
- An integer n (1 ≤ n ≤ 9)

**Output:**
- A number pyramid pattern

**Sample Input:**
```
5
```

**Sample Output:**
```
1
12
123
1234
12345
```

---

## Problem 3: String Reverser and Counter
**Topics:** Strings (string handling), Predefined string functions, Arrays

**Problem Description:**
Write a program that takes a string input, reverses it, and counts the number of vowels (a, e, i, o, u - case insensitive) in the original string.

**Input:**
- A string (max 100 characters)

**Output:**
- The reversed string
- The number of vowels

**Sample Input:**
```
CodeChum
```

**Sample Output:**
```
Reversed: muhCedoC
Vowels: 3
```

---

## Problem 4: Temperature Converter with Switch
**Topics:** Switch statement, Typecasting, Arithmetic operators, Predefined math functions

**Problem Description:**
Create a temperature converter that converts between Celsius, Fahrenheit, and Kelvin. The user chooses the conversion type using a menu.

**Input:**
- Choice (1-6)
- Temperature value (float)

**Menu:**
```
1. Celsius to Fahrenheit
2. Celsius to Kelvin
3. Fahrenheit to Celsius
4. Fahrenheit to Kelvin
5. Kelvin to Celsius
6. Kelvin to Fahrenheit
```

**Output:**
- Converted temperature (2 decimal places)

**Sample Input:**
```
1
25.0
```

**Sample Output:**
```
77.00
```

---

## Problem 5: Array Statistics Calculator
**Topics:** One-dimensional arrays, Array traversal, Arithmetic operators, Predefined math functions

**Problem Description:**
Write a program that reads n integers into an array and calculates the sum, average, maximum, and minimum values.

**Input:**
- An integer n (number of elements, 1 ≤ n ≤ 100)
- n integers

**Output:**
- Sum of all elements
- Average (2 decimal places)
- Maximum value
- Minimum value

**Sample Input:**
```
5
10 25 8 42 15
```

**Sample Output:**
```
Sum: 100
Average: 20.00
Maximum: 42
Minimum: 8
```

---

## Problem 6: Bitwise Operations Explorer
**Topics:** Bitwise operators, Output operations, Selection structures

**Problem Description:**
Write a program that performs various bitwise operations on two integers and displays the results.

**Input:**
- Two integers a and b

**Output:**
- a AND b
- a OR b
- a XOR b
- NOT a (bitwise complement)
- a left shift by 1
- b right shift by 1

**Sample Input:**
```
12
5
```

**Sample Output:**
```
AND: 4
OR: 13
XOR: 9
NOT a: -13
Left Shift a: 24
Right Shift b: 2
```

---

## Problem 7: Matrix Addition
**Topics:** Two-dimensional arrays, Nested loops, Array traversal, Arithmetic operators

**Problem Description:**
Write a program that reads two matrices (2D arrays) of the same dimensions and computes their sum.

**Input:**
- Two integers r and c (rows and columns, 1 ≤ r, c ≤ 10)
- r×c integers for first matrix
- r×c integers for second matrix

**Output:**
- The resulting matrix after addition

**Sample Input:**
```
2 3
1 2 3
4 5 6
7 8 9
10 11 12
```

**Sample Output:**
```
8 10 12
14 16 18
```

---

## Problem 8: Character Analysis Tool
**Topics:** Predefined character functions, While loop, Break/Continue, Boolean operators

**Problem Description:**
Write a program that analyzes a string character by character until it encounters a period (.) or reaches the end. Count uppercase letters, lowercase letters, digits, and spaces. Skip special characters (don't count them).

**Input:**
- A string (max 200 characters)

**Output:**
- Number of uppercase letters
- Number of lowercase letters
- Number of digits
- Number of spaces

**Sample Input:**
```
Hello World 2025!
```

**Sample Output:**
```
Uppercase: 2
Lowercase: 8
Digits: 4
Spaces: 2
```

---

## Problem 9: Simple Calculator with Nested Decisions
**Topics:** Nested decision structures, Arithmetic operators, Selection structures

**Problem Description:**
Create a calculator that performs basic operations (+, -, *, /, %). The program should validate that division/modulo by zero is not allowed.

**Input:**
- Two numbers (float)
- An operator character (+, -, *, /, %)

**Output:**
- Result of the operation (2 decimal places)
- Error message if division/modulo by zero

**Sample Input:**
```
10
5
+
```

**Sample Output:**
```
Result: 15.00
```

**Sample Input 2:**
```
10
0
/
```

**Sample Output 2:**
```
Error: Division by zero
```

---

## Problem 10: Prime Number Checker with For Loop
**Topics:** For loop, Boolean operators, Relational operators, Break statement

**Problem Description:**
Write a program that checks if a given number is prime. A prime number is greater than 1 and has no divisors other than 1 and itself.

**Input:**
- An integer n (1 ≤ n ≤ 10000)

**Output:**
- "Prime" if the number is prime
- "Not Prime" otherwise

**Sample Input:**
```
17
```

**Sample Output:**
```
Prime
```

**Sample Input 2:**
```
18
```

**Sample Output 2:**
```
Not Prime
```

---

## Problem 11: Escape Sequence Formatter
**Topics:** Escape sequences, Output operations, String handling

**Problem Description:**
Write a program that displays a formatted receipt with proper alignment using tabs and newlines. Read item names, quantities, and prices, then display a formatted receipt.

**Input:**
- Integer n (number of items, 1 ≤ n ≤ 5)
- For each item: name (string), quantity (int), price (float)

**Output:**
- Formatted receipt with tabs between columns

**Sample Input:**
```
3
Apple 5 20.50
Banana 10 15.00
Orange 3 25.75
```

**Sample Output:**
```
ITEM		QTY	PRICE	TOTAL
Apple		5	20.50	102.50
Banana		10	15.00	150.00
Orange		3	25.75	77.25
-----------------------------------
GRAND TOTAL:		329.75
```

---

## Problem 12: Assignment Operators Practice
**Topics:** Assignment operators (+=, -=, *=, /=, %=), Output operations

**Problem Description:**
Write a program that demonstrates all assignment operators. Start with an initial value and perform a series of operations using compound assignment operators.

**Input:**
- An integer n (initial value)
- Five integers representing values to: add, subtract, multiply, divide, and modulo

**Output:**
- Result after each operation

**Sample Input:**
```
100
50
20
2
5
3
```

**Sample Output:**
```
After +=: 150
After -=: 130
After *=: 260
After /=: 52
After %=: 1
```

---

## Problem 13: String Concatenation and Comparison
**Topics:** Predefined string functions, Relational operators, String handling

**Problem Description:**
Write a program that takes two strings and performs various string operations: concatenation, length comparison, and alphabetical comparison.

**Input:**
- Two strings (max 50 characters each)

**Output:**
- Concatenated string
- Which string is longer (or "Equal length")
- Which string comes first alphabetically

**Sample Input:**
```
Hello
World
```

**Sample Output:**
```
Concatenated: HelloWorld
Hello is shorter
Hello comes first alphabetically
```

---

## Problem 14: Fibonacci Sequence Generator
**Topics:** While loop, Arrays, Arithmetic operators

**Problem Description:**
Generate the first n numbers of the Fibonacci sequence and store them in an array. Display the sequence and the sum of all numbers.

**Input:**
- An integer n (1 ≤ n ≤ 20)

**Output:**
- The Fibonacci sequence
- Sum of all numbers in the sequence

**Sample Input:**
```
7
```

**Sample Output:**
```
Sequence: 0 1 1 2 3 5 8
Sum: 20
```

---

## Problem 15: Grade Distribution System
**Topics:** Arrays, For loop, If-else if-else statement, Relational operators

**Problem Description:**
Write a program that reads n student grades and categorizes them into grade brackets: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60). Display how many students fall into each category.

**Input:**
- Integer n (number of students, 1 ≤ n ≤ 50)
- n integers (grades, 0-100)

**Output:**
- Count of students in each grade bracket

**Sample Input:**
```
8
95 87 76 92 65 58 81 73
```

**Sample Output:**
```
A: 2
B: 2
C: 2
D: 1
F: 1
```

---

## Problem 16: Matrix Transpose
**Topics:** Two-dimensional arrays, Nested loops, Array traversal

**Problem Description:**
Write a program that reads a matrix and displays its transpose (rows become columns and vice versa).

**Input:**
- Two integers r and c (rows and columns, 1 ≤ r, c ≤ 10)
- r×c integers

**Output:**
- The transposed matrix (c×r)

**Sample Input:**
```
3 2
1 2
3 4
5 6
```

**Sample Output:**
```
1 3 5
2 4 6
```

---

## Problem 17: Power Calculator with Math Functions
**Topics:** Predefined math functions, For loop, Typecasting

**Problem Description:**
Write a program that calculates the power of a number using both a loop and the built-in power function. Display both results and verify they match.

**Input:**
- Two integers: base and exponent (0 ≤ exponent ≤ 10)

**Output:**
- Result using loop
- Result using math function
- "Match" or "No Match"

**Sample Input:**
```
2
5
```

**Sample Output:**
```
Loop result: 32
Math function result: 32.00
Match
```

---

## Problem 18: Number Guessing with Break and Continue
**Topics:** While loop, Break, Continue, Relational operators, Boolean operators

**Problem Description:**
Create a number guessing game where the user has 5 attempts to guess a secret number between 1 and 50. Use continue for invalid inputs (outside range) and break when guessed correctly.

**Input:**
- Secret number (1-50)
- Up to 5 guesses

**Output:**
- Hints ("Too high" or "Too low") for each guess
- "Correct!" when guessed
- "Game over" if not guessed in 5 attempts

**Sample Input:**
```
25
30
20
25
```

**Sample Output:**
```
Too high
Too low
Correct! You guessed in 3 attempts.
```

---

## Problem 19: Palindrome Checker
**Topics:** String handling, Predefined string functions, For loop, Boolean operators

**Problem Description:**
Write a program that checks if a given string is a palindrome (reads the same forwards and backwards). Ignore spaces and case.

**Input:**
- A string (max 100 characters)

**Output:**
- "Palindrome" or "Not a palindrome"

**Sample Input:**
```
A man a plan a canal Panama
```

**Sample Output:**
```
Palindrome
```

**Sample Input 2:**
```
Hello
```

**Sample Output 2:**
```
Not a palindrome
```

---

## Problem 20: Student Record System
**Topics:** Two-dimensional arrays, Arrays, String handling, Nested loops, Selection structures

**Problem Description:**
Create a simple student record system that stores names and three test scores for n students. Calculate and display each student's average and overall class average.

**Input:**
- Integer n (number of students, 1 ≤ n ≤ 10)
- For each student: name (string) and three test scores (integers)

**Output:**
- Each student's name and average (2 decimal places)
- Class average (2 decimal places)

**Sample Input:**
```
3
Alice 85 90 88
Bob 78 82 80
Charlie 92 95 93
```

**Sample Output:**
```
Alice: 87.67
Bob: 80.00
Charlie: 93.33
Class Average: 87.00
```

---
