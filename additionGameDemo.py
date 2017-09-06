#Charlie Goodrich
#09/06/17
#additionGameDemo.py - our first game

from random import randint

num1 = randint(1,10)
num2 = randint(1,10)
answer = int(input(str(num1) + " + " + str(num2) + " = "))
print(answer == num1 + num2)