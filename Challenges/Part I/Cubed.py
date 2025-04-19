# Module for Chapter 8 challenges.
import math

def cubed_num(number):
    try:
        number = float(number)
        return math.pow(number, 3)
    except:
        print("Value isn't a number...")