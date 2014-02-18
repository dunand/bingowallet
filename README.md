bingowallet
===========

This simple utility to help you generate a super secure Bitcoin Private key using anything you have to pick random numbers. A dice, a coin, a bag of marbles. I writed this script because I wanted to generate a bitcoin Private key using bingo balls numbered from 1 to 75.

Example of use:
<pre>
$ python bingowallet.py 

This program will help you generate a Bitcoin private key using a simple random number generator like a dice, a coin or a bag of bingo balls!

The first step is to pick a base.
If you use a 6 sided dice, choose 6.
If you use a 12 sided dice, choose 12.
If you want to use a coin, choose 2.
If you want to pick bingo balls in a bag you choose 75...
Your base: 75

Now you need to choose if you start to count at 0 or 1. For example, if you use a dice numbered from 1 to 6, choose 1.
You want to start to count at 0 or 1: 1

OK, now it's time for you to start picking numbers randomly
You need to pick 42 numbers to generate 256 bits of randomness
Enter each number one by one. Valid number is 1 to 75

#1: 19
#2: 13
#3: 9
#4: 57
#5: 44
#6: 10
#7: 35
#8: 50
#9: 9
#10: 6
#11: 41
#12: 53
#13: 32
#14: 2
#15: 5
#16: 45
#17: 48
#18: 7
#19: 73
#20: 1
#21: 70
#22: 46
#23: 59
#24: 3
#25: 67
#26: 26
#27: 18
#28: 44
#29: 8
#30: 55
#31: 38
#32: 27
#33: 35
#34: 8
#35: 75
#36: 453
Each character typed must be a numeral 1 - 75.  Try again.
#36: 45
#37: 3
#38: 56
#39: 25
#40: 23
#41: 61
#42: 6

Private key Binary Format:
1111000111110100111101111100110000000101000110010011110100010100101001111111101110101111010110111100100001110001010000100000010110101001101000011110101001000001101111001010010111010010100000111011110111011111101111111111001110010010101000101101101110101001

Private Key Hexadecimal Format (64 characters [0-9A-F]):
F1F4F7CC05193D14A7FBAF5BC8714205A9A1EA41BCA5D283BDDFBFF392A2DBA9

Private key Base64 (44 characters):
8fT3zAUZPRSn+69byHFCBamh6kG8pdKDvd+/85Ki26k=
</pre>
