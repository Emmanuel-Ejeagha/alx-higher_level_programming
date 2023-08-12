#!/usr/bin/python3
def fizzbuzz():
    """This numbers from 1 to 100 seperated by a space"""
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 != 0:
            print("Fizz", end=" ")
        elif number % 5 == 0 and number % 3 != 0:
            print("Buzz", end=" ")
        elif number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end=" ")
        else:
            print(number, end=" ")
