bingowallet
===========

Python script for generating Bitcoin Private key from randomly picking Bingo balls from 1 to 64.
This simple utility help you generate a super secure Bitcoin Private key using bingo balls numbered 1 to 64. Before beginning you must discard bingo balls higher than 64. You only keep balls from 1 to 64. Remember to always put back the last picked ball in the hat between each pick. 

Example of use:
<code>
$ python bingowallet.py 

OK, now it's time for you to start picking bingo balls randomly
You need to pick 43 balls to generate 256 bits of randomness
Enter each ball number one by one. Valid number is 1 to 64
Remember to always put back the last picked ball in the hat between each pick

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
#14: 34
#15: 2
#16: 5
#17: 45
#18: 48
#19: 7
#20: 47
#21: 46
#22: 47
#23: 59
#24: 3
#25: 60
#26: 26
#27: 60
#28: 49
#29: 16
#30: 35
#31: 5
#32: 31
#33: 12
#34: 59
#35: 4056
Each character typed must be a numeral 1-64.  Try again.
#35: 40
#36: 56
#37: 5
#38: 37
#39: 55
#40: 38
#41: 35
#42: 8
#43: 21

Private key Binary Format:
010010001100001000111000101011001001100010110001001000000101101000110100011111100001000001000100101100101111000110101110101101101110111010000010111011011001111011110000001111100010000100011110001011111010100111110111000100100100110110100101100010000111010100

Private key Base64 (44 characters):
SMI4rJixIFo0fhBEsvGutu6C7Z7wPiEeL6n3Ek2liHU=

Private Key Hexadecimal Format (64 characters [0-9A-F]):
48c238ac98b1205a347e1044b2f1aeb6ee82ed9ef03e211e2fa9f7124da58875
</code>
