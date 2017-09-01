#Charlie Goodrich
#09/01/17
#pythagoreanDemo.py - program that does the pythagorean theorem

from math import sqrt

a = float(input("Enter leg 1: "))
b = float(input("Enter leg 2: "))
print("The hypotenuse is", sqrt(a**2 + b**2))
