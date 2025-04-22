# ax**+bx+c = 0
import cmath

a = int(input("Enter number (a!=0) : "))
b = int(input("Enter number b : "))
c = int(input("Enter number c : "))

d = (b**2) - (4 * a * c)

root1 = (-b - cmath.sqrt(d)) / (2 * a)
root2 = (-b + cmath.sqrt(d)) / (2 * a)
print(f"The value {root1} , {root2}")
