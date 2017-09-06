#Charlie Goodrich
#09/06/17
#isItATriangle.py - tells you if you have a triangle

side1 = float(input("Enter side A: "))
side2 = float(input("Enter side B: "))
side3 = float(input("Enter side C: "))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("You've got a triangle!")
else:
    print("You don't have a triangle :'(")



