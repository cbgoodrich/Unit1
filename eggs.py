#Charlie Goodrich
#09/06/17
#eggs.py - gives you the number of cartons for eggs

eggs = int(input("How many eggs do you have? "))
carton = int(input("How many cartons do you have? "))

cartonReal = eggs//12 +1

print(cartonReal == carton)