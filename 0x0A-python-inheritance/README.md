# Python Inheritance Tasks

Welcome to the Python Inheritance task repository! This repository contains a series of Python programming tasks focused on object-oriented programming and inheritance. These tasks are designed to test your understanding of Python's class inheritance and object-oriented principles.

## Task 0: Lookup

In this task, you are required to write a Python function that returns a list of available attributes and methods of an object. You must not import any modules. Here's how you can use the function:

```python
from 0-lookup import lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))


Task 1: My List
For this task, you need to create a class called MyList that inherits from the built-in Python list. You must implement a method print_sorted that prints the list in ascending order. It is assumed that all elements of the list will be of type int.

Task 2: Exact Same Class
In this task, you should write a function is_same_class that returns True if an object is exactly an instance of the specified class and False otherwise.

Task 3: Same Class or Inherit From
Write a function is_kind_of_class that returns True if an object is an instance of, or if the object is an instance of a class that inherited from, the specified class.

Task 4: Only Sub Class Of
Create a function inherits_from that returns True if an object is an instance of a class that inherited (directly or indirectly) from the specified class.

Task 5: Geometry Module
For this task, you need to create an empty class called BaseGeometry. No additional modules should be imported.

Task 6: Improve Geometry
Extend the BaseGeometry class from Task 5. Add a public instance method area(self) that raises an Exception with the message "area() is not implemented."

Task 7: Integer Validator
Extend the BaseGeometry class from Task 6. Add a public instance method integer_validator(self, name, value) that validates the value argument. If value is not an integer, it should raise a TypeError exception with the message <name> must be an integer. If value is less than or equal to 0, it should raise a ValueError exception with the message <name> must be greater than 0.

Task 8: Rectangle
Create a class Rectangle that inherits from BaseGeometry (from Task 7). The Rectangle class should be instantiated with width and height, which must be positive integers and validated using the integer_validator method. The Rectangle class should not have getter or setter methods for width and height.

Task 9: Full Rectangle
Extend the Rectangle class from Task 8. Implement the area() method to calculate the area of the rectangle. The print() method should print, and str() should return, the rectangle's description in the format [Rectangle] <width>/<height>.

Task 10: Square #1
Create a class Square that inherits from Rectangle (from Task 9). The Square class should be instantiated with a single argument size, which must be a positive integer and validated using the integer_validator method. The Square class should not have getter or setter methods for size.

Task 11: Square #2
Extend the Square class from Task 10. The print() method should print, and str() should return, the square's description in the format [Square] <width>/<height>.

Task 12: My Integer
Create a class MyInt that inherits from the built-in int class. In this custom class, the == and != operators should be inverted.

Task 13: Can I?
Write a function add_attribute that adds a new attribute to an object if it's possible. If it's not possible, the function should raise a TypeError exception with the message "can't add new attribute."

We encourage you to tackle these tasks and test your Python programming skills related to object-oriented programming and inheritance. Happy coding!

