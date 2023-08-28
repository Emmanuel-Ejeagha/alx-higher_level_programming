# Python Exception Handling Exercises :snake: :large_blue_circle:

This repository contains a collection of Python exercises focused on exception handling. Each exercise is designed to help you practice handling various types of exceptions and errors in Python.

## Table of Contents

- [Task 0: Safe List Printing](#task-0-safe-list-printing)
- [Task 1: Safe Printing of an Integers List](#task-1-safe-printing-of-an-integers-list)
- [Task 2: Print and Count Integers](#task-2-print-and-count-integers)
- [Task 3: Integers Division with Debug](#task-3-integers-division-with-debug)
- [Task 4: Divide a List](#task-4-divide-a-list)
- [Task 5: Raise Exception](#task-5-raise-exception)
- [Task 6: Raise Exception with Message](#task-6-raise-exception-with-message)
- [Task 7: Safe Integer Print with Error Message](#task-7-safe-integer-print-with-error-message)
- [Task 8: Safe Function](#task-8-safe-function)
- [Task 9: ByteCode to Python](#task-9-bytecode-to-python)
- [Task 10: CPython PyFloatObject](#task-10-cpython-pyfloatobject)

## Task 0: Safe List Printing

Implement a function `safe_print_list(my_list=[], x=0)` that prints x elements of a list. The function should handle exceptions and print the elements safely. For more details, see [Task 0](./0-safe_print_list.py).

## Task 1: Safe Printing of an Integers List

Write a function `safe_print_integer(value)` that prints an integer using the format "{:d}". The function should handle exceptions and return True if successful, otherwise False. For more details, see [Task 1](./1-safe_print_integer.py).

## Task 2: Print and Count Integers

Create a function `safe_print_list_integers(my_list=[], x=0)` that prints the first x integer elements of a list. The function should handle exceptions and return the count of printed integers. For more details, see [Task 2](./2-safe_print_list_integers.py).

<!-- Python Exceptions Continues -->

## Task 3: Integers Division with Debug

Write a function `safe_print_division(a, b)` that divides two integers and prints the result. The function should use try, except, and finally blocks to handle exceptions. For more details, see [Task 3](./3-safe_print_division.py).

## Task 4: Divide a List

Implement a function `list_division(my_list_1, my_list_2, list_length)` that divides two lists element by element. The function should handle various cases and exceptions. For more details, see [Task 4](./4-list_division.py).

## Task 5: Raise Exception

Create a function `raise_exception()` that raises a type exception. For more details, see [Task 5](./5-raise_exception.py).

## Task 6: Raise Exception with Message

Write a function `raise_exception_msg(message="")` that raises a name exception with a custom message. For more details, see [Task 6](./6-raise_exception_msg.py).

## Task 7: Safe Integer Print with Error Message

Implement a function `safe_print_integer_err(value)` that prints an integer. If an exception occurs, the function should return False and print an error message to stderr. For more details, see [Task 7](./100-safe_print_integer_err.py).

## Task 8: Safe Function

Create a function `safe_function(fct, *args)` that executes a function safely and returns the result. The function should handle exceptions and print error messages if needed. For more details, see [Task 8](./101-safe_function.py).

## Task 9: ByteCode to Python

Write the Python function `magic_calculation(a, b)` that replicates a given Python bytecode. The function's implementation can be found in [Task 9](./102-magic_calculation.py).

## Task 10: CPython PyFloatObject :snake: :large_blue_circle:

This task involves creating C functions to print information about Python lists, bytes, and float objects. For more details, see [Task 10](./103-python.c).

