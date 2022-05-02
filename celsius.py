#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on May 2022
# This is a program that converts celsius to fahrenheit


def fahrenheit():
    # This convets Celsius to Fahrenheit

    # Input
    celsius_string = input("Enter a Tempature in Celsius: ")

    # Process
    try:
        celsius_float = float(celsius_string)
        fahrenheit_float = celsius_float * 1.8 + 32
        print("{0} celsius = {1} fahrenheit".format(celsius_float, fahrenheit_float))
    except Exception:
        print("You Messed Up!")
    finally:
        print("\nDone.")


def main():
    # This is the main function

    # Call functions
    fahrenheit()


if __name__ == "__main__":
    main()
