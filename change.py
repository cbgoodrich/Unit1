#Charlie Goodrich
#09/06/17
#change.py - gives you your change

changeTotal = int(input("How many cents do you have? "))

quarterNum = changeTotal//25
dimeNum = (changeTotal - quarterNum*25)//10
nickelNum = (changeTotal - quarterNum*25 - dimeNum*10)//5
pennyNum = (changeTotal - quarterNum*25 - dimeNum*10 - nickelNum*5)//1

print("Quarters:", quarterNum)
print("Dimes:", dimeNum)
print("Nickels:", nickelNum)
print("Pennies:", pennyNum)