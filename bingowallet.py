#|========================================================================
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

import math

min_value = '0000000000000000000000000000000000000000000000000000000000000001'
max_value = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141'
max_value_int = int(max_value, base=16)
base_64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
priv_bin = ''
priv_hex = ''
priv_base_64 = ''

try:
    input = raw_input
except NameError:
    pass


def is_valid_number(s, min_value, max_value):
    try:
        number = int(s)
        return number >= min_value and number <= max_value
    except ValueError:
        return False


def input_number(message, min_value, max_value):
    while True:
        num_dec = input(message)
        if is_valid_number(num_dec, min_value, max_value):
            num_dec = int(num_dec)
            problem = False
        else:
            print("Each character typed must be a numeral " +
                  str(min_value) + " - " + str(max_value) + ".  Try again.")
            problem = True
        if not problem:
            break
    return num_dec

print(
    "\nThis program will help you generate a Bitcoin private key using a simple random number generator like a dice, a coin or a bag of bingo balls!")
print("\nThe first step is to pick a base.")
print("If you use a 6 sided dice, choose 6.")
print("If you use a 12 sided dice, choose 12.")
print("If you want to use a coin, choose 2.")
print("If you want to pick bingo balls in a bag you choose 75...")

base = input_number("Your base: ", 2, 2 ** 256)
how_many_pick = int(math.ceil(math.log(max_value_int, base)))

print(
    "\nNow you need to choose if you start to count at 0 or 1. For example, if you use a dice numbered from 1 to 6, choose 1.")

start_numbering = input_number("You want to start to count at 0 or 1: ", 0, 1)
valid_input_max = base - 1 + start_numbering

print("\nOK, now it's time for you to start picking numbers randomly")
print("You need to pick " + str(how_many_pick)
      + " numbers to generate 256 bits of randomness")
print("Enter each number one by one. Valid number is " +
      str(start_numbering) + " to " + str(valid_input_max) + "\n")

priv_dec = 0
for i in range(how_many_pick):
    num_dec = input_number(
        "#" + str(i + 1) + ": ",
        start_numbering,
        valid_input_max) - start_numbering
    priv_dec += num_dec * base ** i

priv_bin = "{0:0256b}".format(priv_dec)[0:256]
print("\nPrivate key Binary Format:")
print(priv_bin)

for i in range(64):
    num_bin = priv_bin[i * 4:(i + 1) * 4]
    num_hex = hex(int(num_bin, 2))[2:]
    priv_hex += num_hex.upper()

print("\nPrivate Key Hexadecimal Format (64 characters [0-9A-F]):")
print(priv_hex)

for i in range(43):
    num_bin = priv_bin[i * 6:(i + 1) * 6]
    if i < 42:
        num_dec = int(num_bin, 2)
    else:
        num_bin = num_bin[0:4]
        num_dec = int(num_bin + '00', 2)
    priv_base_64 += base_64[num_dec]
priv_base_64 += '='

print("\nPrivate key Base64 (44 characters):")
print(priv_base_64)

if priv_hex < min_value or priv_hex > max_value:
    print(
        "\nYOU ARE VERY BAD AT PICKING UP RANDOM BALLS. YOUR PRIVATE KEY IS INVALID")
