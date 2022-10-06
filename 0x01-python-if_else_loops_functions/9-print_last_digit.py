#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * (-1)
        digit = number % 10
        return digit
    else:
        digit = number % 10
        print(digit)