#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Nov. 24, 2022
# This program asks for a temperature
# in celsius and shows the user what
# it is converted into fahrenheit

import math


def main():
    # introductory paragraph
    print("This program asks for a temperature")
    print("in celsius and shows the user what")
    print("it is converted into fahrenheit")
    print("")

    # input
    # getting user_num_string
    cel_temp = input("Enter a temperature: ")

    # fahrenheit function
    def fahrenheit():
        # calculating fah_temp
        fah_temp = (9 / 5) * cel_temp + 32

        # printing results
        print("\n")
        print("Your temperature in fahrenheit is ", end="")
        print("%.2f" % fah_temp, end="")
        print(".")

    # process
    # checking that user_num_string is an integer
    try:
        # checking that cel_temp isn't a string
        cel_temp = float(cel_temp)

        # calling fahrenheit()
        fahrenheit()
    except ValueError:
        print("\n")
        print(("Please enter a valid temperature."))
    finally:
        print("Thanks for converting!")


if __name__ == "__main__":
    main()
