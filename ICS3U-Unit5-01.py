#!/usr/bin/env python3

# Created by: Emmanuel
# Created on: Nov 2022
# This program uses user defined functions

import math


def fahrenheit():
    # this function takes temp in degrease celsius 
    # and converts it into fahrenheit.

    # input
    celsius_string = input("Enter a temperature (°C): ")

    try:
        print("")
        celsius_temp = float(celsius_string)
        fahrenheit_temp = 9 / 5 * celsius_temp + 32
        print("{0}°C is equal to {1:.2f}°F.".format(celsius_temp, fahrenheit_temp))

    except ValueError:
        print("{0}, is invalid input please try again.".format(celsius_string))

    print("\n\nDone.")


def main():
    fahrenheit()

    
if __name__ == "__main__":
    main()
