#TEST_DRIVEN DEVELOPMENT

## Introduction

Welcome to my GitHub repository for the Alx Higher Level Programming project on Test-Driven Development in Python. This project showcases my expertise in Python programming, software testing, and problem-solving. Each task in this project demonstrates my ability to write efficient and reliable Python code while adhering to best practices in software development.

## Task 0: Integers Addition

In this task, I've implemented a Python function `add_integer` that adds two integers. Here are the details of the task:

- Prototype: `def add_integer(a, b=98):`
- Both `a` and `b` must be integers or floats, otherwise, a `TypeError` exception is raised.
- If `a` or `b` is a float, they are first casted to integers.
- The function returns the addition of `a` and `b`.
- No external modules are imported.

You can test the function using the provided test cases in `0-main.py` and `tests/0-add_integer.txt`.

## Task 1: Divide a Matrix

In this task, I've implemented a Python function `matrix_divided` that divides all elements of a matrix. Here are the details:

- Prototype: `def matrix_divided(matrix, div):`
- `matrix` must be a list of lists of integers or floats, otherwise, a `TypeError` exception is raised.
- Each row of the matrix must have the same size, or a `TypeError` exception is raised.
- `div` must be a number (integer or float), or a `TypeError` exception is raised.
- `div` cannot be equal to 0, or a `ZeroDivisionError` exception is raised.
- All elements of the matrix are divided by `div` and rounded to 2 decimal places.
- The function returns a new matrix.
- No external modules are imported.

You can test the function using the provided test cases in `2-main.py` and `tests/2-matrix_divided.txt`.

## Task 2: Say My Name

In this task, I've implemented a Python function `say_my_name` that prints "My name is <first name> <last name>". Here are the details:

- Prototype: `def say_my_name(first_name, last_name=""):`
- Both `first_name` and `last_name` must be strings, or a `TypeError` exception is raised.
- The function prints the formatted name.
- No external modules are imported.

You can test the function using the provided test cases in `3-main.py` and `tests/3-say_my_name.txt`.

## Task 3: Print Square

In this task, I've implemented a Python function `print_square` that prints a square with the character '#'. Here are the details:

- Prototype: `def print_square(size):`
- `size` is the size length of the square.
- `size` must be an integer, otherwise, a `TypeError` exception is raised.
- If `size` is less than 0, a `ValueError` exception is raised.
- The function prints the square.
- No external modules are imported.

You can test the function using the provided test cases in `4-main.py` and `tests/4-print_square.txt`.

## Task 4: Text Indentation

In this task, I've implemented a Python function `text_indentation` that prints a text with 2 new lines after each '.', '?', and ':'. Here are the details:

- Prototype: `def text_indentation(text):`
- `text` must be a string, otherwise, a `TypeError` exception is raised.
- The function prints the formatted text with proper indentation.
- No external modules are imported.

You can test the function using the provided test cases in `5-main.py` and `tests/5-text_indentation.txt`.

## Task 5: Max Integer - Unittest

In this task, I've written unittests for the `max_integer` function. The test cases cover various scenarios to ensure the function works correctly. You can find the unittests in `tests/6-max_integer_test.py`. To run the tests, use the command `python3 -m unittest tests.6-max_integer_test`.

## Task 6: Matrix Multiplication

In this task, I've implemented a Python function `matrix_mul` that multiplies two matrices. The function adheres to strict validation rules to ensure the matrices can be multiplied. You can find the details and test cases in `100-matrix_mul.py` and `tests/100-matrix_mul.txt`.

## Task 7: Lazy Matrix Multiplication

In this task, I've implemented a Python function `lazy_matrix_mul` that multiplies two matrices using the NumPy module. The function has the same functionality as Task 6 but utilizes NumPy for efficiency. You can find the details and test cases in `101-lazy_matrix_mul.py` and `tests/101-lazy_matrix_mul.txt`.

## Task 8: CPython #3 - Python Strings

In this advanced task, I've created a CPython extension module that prints Python strings. The module uses the C standard library and demonstrates Python string handling in C. You can find the C code in `102-python.c`, along with the test script in `102-tests.py`.

## Conclusion

This repository showcases my proficiency in Python programming and software testing. Each task is implemented following best practices and thoroughly tested to ensure correctness. Feel free to explore the code and test cases to see my skills in action. If you have any questions or would like to discuss potential employment opportunities, please don't hesitate to contact me. Thank you for considering my application!
