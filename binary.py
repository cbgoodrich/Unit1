#Charlie Goodrich
#09/08/17
#binary.py - converts binary to decimal

binaryNumber = int(input("Enter an 8-digit binary number (0s and 1s): "))

ones = binaryNumber%10
twos = (binaryNumber//10)%10
threes = (binaryNumber//100)%10
fours = (binaryNumber//1000)%10
fives = (binaryNumber//10000)%10
sixes = (binaryNumber//100000)%10
sevens = (binaryNumber//1000000)%10
eights = (binaryNumber//10000000)%10

decimalNumber = ((ones*2**0) + (twos*2**1) + (threes*2**2) + (fours*2**3) + 
                (fives*2**4) + (sixes*2**5) + (sevens*2**6) + (eights*2**7))

print(decimalNumber)


