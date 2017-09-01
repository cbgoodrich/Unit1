#Charlie Goodrich
#09/01/17
#tipCalculator.py - calculates tip given price of meal

mealPrice = float(input("Price of meal (in USD) "))
tipValue = float(input("Enter tip value "))

tipCost = mealPrice*tipValue/100

print("You should tip", round(tipCost, 2), "dollars.")
