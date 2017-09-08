#Charlie Goodrich
#09/06/17
#isItATriangle.py - tells you if you have a triangle

side1 = float(input("Enter side A: "))
side2 = float(input("Enter side B: "))
side3 = float(input("Enter side C: "))

bigSide = max(side1, side2, side3)
smallSide = min(side1, side2, side3)

perimeter = side1 + side2 + side3
middleSide = perimeter - bigSide - smallSide

print(middleSide + smallSide > bigSide)
