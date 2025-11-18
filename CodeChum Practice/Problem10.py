# Write a program that checks if a given number is prime. A prime number is greater than 1 and has no divisors other than 1 and itself.
num = abs(int(input()))
notPrime = False
nope = True

for i in range(2, num, 1):
    if num > 10000:
        nope = False
        break
    elif (num % i) == 0:
        notPrime = True
        break

if nope == False:
    print("Too much bro")
elif notPrime == True:
    print("Not prime")
else:
    print("Is prime")