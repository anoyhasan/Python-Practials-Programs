import math

num = int(input("Enter a Number : "))

if num < 0:
    print("Negative Number")
else:
    fac = math.factorial(num)
    print(f"The factorial of {num} number is {fac}")
