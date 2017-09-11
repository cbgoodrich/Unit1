#Charlie Goodrich
#09/11/17
#quiz1.py - my first quiz -- prints name, and lucky number

name = "Charlie Goodrich"

print(name)

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

numSum = num1 + num2
numProduct = num1 * num2

luckyNum = (num1 * 7) + (num2 * 7)

print("The sum is", numSum)
print("The product is", numProduct)
print("Your lucky number is", luckyNum)