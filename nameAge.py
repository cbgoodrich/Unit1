#Charlie Goodrich
#09/01/17
#nameAge.py - tells you how old you will be, how many letters in name

fullName = input("Enter your first and last name ")
age = int(input("Enter your age "))

var1, var2 = fullName.split()
print("Your first name has", len(var1), "letters.")
print("Your last name has", len(var2), "letters.")
print("You will be", age+1, "years old next year")

