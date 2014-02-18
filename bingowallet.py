#|=========================================================================================
#|
#|   bingowallet.py                                           [Python console script]
#|
#|       This simple utility to help you generate a super secure Bitcoin Private key using
#|       anything you have to pick random numbers. A dice, a coin, a bag of marbles. I 
#|       writed this script because I wanted to generate a bitcoin private key using bingo
#|       balls numbered from 1 to 75.
#|
#|   Language:   Python version 2.x
#|                   (Tested with 2.7.5+ & 3.3.2+ on Ubuntu 13.10)       
#|
#|   Licensing:
#|       GPLv2 (http://opensource.org/licenses/GPL-2.0)
#|
#|vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

import time

MIN_VALUE = '0000000000000000000000000000000000000000000000000000000000000001'
MAX_VALUE = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141'
base64 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
privBin = ''
privHex = ''
privB64 = ''

try: 
	input = raw_input
except NameError: 
	pass

def isValidNumber(s, minValue, maxValue):
    try:
        number = int(s)
        return number >= minValue and number <= maxValue
    except ValueError:
        return False

def haveEnoughRandomBits(base, exp):
	return base**exp >= 2**256

def howManyPickForFullEntropy(base):
	i = 0
	while not haveEnoughRandomBits(base, i):
		i += 1
	return i

def inputNumber(message, minValue, maxValue):
	while True:
		numDec = input(message)
		if isValidNumber(numDec, minValue, maxValue):
			numDec = int(numDec)
			problem = False
		else:    
			print("Each character typed must be a numeral "+str(minValue)+" - "+str(maxValue)+".  Try again.")
			problem = True
		if not problem:
			break
	return numDec

print("\nThis program will help you generate a Bitcoin private key using a simple random number generator like a dice, a coin or a bag of bingo balls!")
print("\nThe first step is to pick a base.")
print("If you use a 6 sided dice, choose 6.")
print("If you use a 12 sided dice, choose 12.")
print("If you want to use a coin, choose 2.")
print("If you want to pick bingo balls in a bag you choose 75...")

BASE = inputNumber("Your base: ", 2, 2**256)
howManyPick = howManyPickForFullEntropy(BASE);

print("\nNow you need to choose if you start to count at 0 or 1. For example, if you use a dice numbered from 1 to 6, choose 1.")

startNumbering = inputNumber("You want to start to count at 0 or 1: ", 0, 1)
validInputMax = BASE-1+startNumbering

print("\nOK, now it's time for you to start picking numbers randomly")
print("You need to pick "+str(howManyPick)+" numbers to generate 256 bits of randomness")
print("Enter each number one by one. Valid number is "+str(startNumbering)+" to "+str(validInputMax)+"\n")

privDec = 0
i = 0
while not haveEnoughRandomBits(BASE, i):
	numDec = inputNumber("#" + str(i+1) + ": ", startNumbering, validInputMax)-startNumbering
	privDec += numDec * BASE**i
	i+=1

privBin = "{0:0256b}".format(privDec)[0:256]
print("\nPrivate key Binary Format:")
print(privBin)

for i in range(64):
	numBin = privBin[i*4:(i+1)*4]
	numHex = hex(int(numBin, 2))[2:]
	privHex += numHex.upper()

print("\nPrivate Key Hexadecimal Format (64 characters [0-9A-F]):");
print(privHex)

for i in range(43):
	numBin = privBin[i*6:(i+1)*6]
	if i < 42:
		numDec = int(numBin, 2)
	else:
		numBin = numBin[0:4]
		numDec = int(numBin+'00', 2)
	privB64 += base64[numDec]
privB64 += '='

print("\nPrivate key Base64 (44 characters):");
print(privB64)

if privHex < MIN_VALUE or privHex > MAX_VALUE:
	print("\nYOU ARE VERY BAD AT PICKING UP RANDOM BALLS. YOUR PRIVATE KEY IS INVALID")
