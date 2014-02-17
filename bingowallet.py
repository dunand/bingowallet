#|=========================================================================================
#|
#|   bingowallet.py                                           [Python console script]
#|
#|       This simple utility help you generate a super secure Bitcoin Private key using
#|       bingo balls numbered 1 to 64. Before beginning you must discard bingo balls higher
#|       than 64. You only keep balls from 1 to 64. Remember to always put back the last 
#|       picked ball in the hat between each pick. 
#|
#|   Language:   Python version 2.x
#|                   (Tested with 2.7.5+ & 3.3.2+ on Ubuntu 13.10)       
#|
#|   Licensing:
#|       GPLv2 (http://opensource.org/licenses/GPL-2.0)
#|
#|vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

import time;

MIN_VALUE = "00000000000000000000000000000000000000000000000000000000000000001"
MAX_VALUE = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD03641410"
base64 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
privBin = '';
privHex = '';
privBase64 = '';

print("\nOK, now it's time for you to start picking bingo balls randomly");
print("You need to pick 43 balls to generate 256 bits of randomness");
print("Enter each ball number one by one. Valid number is 1 to 64");
print("Remember to always put back the last picked ball in the hat between each pick\n");

def isValidNumber(s):
    try:
        number = int(s);
        return number > 0 and number < 65;
    except ValueError:
        return False;

try: input = raw_input;
except NameError: pass;

for i in range(43):
    while True:
        numDec = input("#" + str(i+1) + ": ");
        if isValidNumber(numDec):
            numDec = int(numDec)-1;
            problem = False;
        else:    
            print("Each character typed must be a numeral 1-64.  Try again.");
            problem = True;
        if not problem:
            break;
    numBin = "{0:06b}".format(numDec);
    if i == 42:
        numBin = numBin[0:4];
        numDec = int(numBin+'00', 2);
    privBin += numBin;
    numBase64 = base64[numDec];
    privBase64 += numBase64;
privBase64 += '=';

print("\nPrivate key Binary Format:");
print(privBin);

print("\nPrivate key Base64 (44 characters):");
print(privBase64);

for i in range(64):
    numBin = privBin[i*4:(i+1)*4];
    numHex = hex(int(numBin, 2))[2:];
    privHex += numHex;

print("\nPrivate Key Hexadecimal Format (64 characters [0-9A-F]):");
print(privHex.upper());

if privHex < MIN_VALUE or privHex > MAX_VALUE:
    print("\nYOU ARE VERY BAD AT PICKING UP RANDOM BALLS. YOUR PRIVATE KEY IS INVALID");


