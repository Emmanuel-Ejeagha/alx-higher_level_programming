imarkdown
Copy code
# Python - Almost a circle

Description of your project.

## Table of Contents

- [Tasks](#tasks)
  - [Task 0: If it's not tested it doesn't work](#task-0-if-its-not-tested-it-doesnt-work)
  - [Task 1: Base class](#task-1-base-class)
  - [Task 2: First Rectangle](#task-2-first-rectangle)
  - [Task 3: Validate attributes](#task-3-validate-attributes)
  - [Task 4: Area first](#task-4-area-first)
  - [Task 5: Display #0](#task-5-display-0)
  - [Task 6: Display #1](#task-6-display-1)
  - [Task 7: Update #0](#task-7-update-0)
  - [Task 8: Update #1](#task-8-update-1)
  - [Task 9: And now, the Square!](#task-9-and-now-the-square)
  - [Task 10: Square size](#task-10-square-size)
  - [Task 11: Square update](#task-11-square-update)
  - [Task 12: Dictionary to JSON string](#task-12-dictionary-to-json-string)
  - [Task 13: Square instance to dictionary representation](#task-13-square-instance-to-dictionary-representation)
  - [Task 14: Dictionary to Instance](#task-14-dictionary-to-instance)
  - [Task 15: File to instances](#task-15-file-to-instances)
  - [Task 16: JSON ok, but CSV?](#task-16-json-ok-but-csv)

## Tasks

### Task 0: If it's not tested it doesn't work
- **Mandatory**
- Score: 0.0% (Checks completed: 0.0%)
- All your files, classes, and methods must be unit tested and be PEP 8 validated.

```shell
guillaume@ubuntu:~/$ python3 -m unittest discover tests
...
Ran 189 tests in 13.135s
OK

- [Task 1: Base class]
Mandatory
Score: 0.0% (Checks completed: 0.0%)
Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package.
Create a file named models/base.py.
python
Copy code
class Base:
    # Class implementation here
Task 2: First Rectangle
Mandatory
Score: 0.0% (Checks completed: 0.0%)
Write the first class Base:
Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package.
Create a file named models/base.py.
Class Base:
Private class attribute __nb_objects = 0.
Class constructor: def __init__(self, id=None).
If id is not None, assign the public instance attribute id with this argument value.
Otherwise, increment __nb_objects and assign the new value to the public instance attribute id.
python
Copy code
class Base:
    # Class implementation here
Task 3: Validate attributes
Mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded):
If the input is not an integer, raise the TypeError exception with the message: <name of the attribute> must be an integer. Example: width must be an integer.
If width or height is under or equals 0, raise the ValueError exception with the message: <name of the attribute> must be > 0. Example: width must be > 0.
If x or y is under 0, raise the ValueError exception with the message: <name of the attribute> must be >= 0. Example: x must be >= 0.
python
Copy code
class Rectangle:
    # Class implementation here
Task 4: Area first
Mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Rectangle by adding the public method def area(self) that returns the area value of the Rectangle instance.
python
Copy code
class Rectangle:
    # Class implementation here

    def area(self):
        # Calculate and return the area here
Task 5: Display #0
Mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Rectangle by adding the public method def display(self) that prints in stdout the Rectangle instance with the character #.
python
Copy code
class Rectangle:
    # Class implementation here

    def display(self):
        # Print the rectangle using '#' characters
...

Task 16: JSON ok, but CSV?
Mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Rectangle by adding the class method def to_csv_string(cls, list_objs) that returns the string representation of a list of Rectangle instances in CSV format.
python
Copy code
class Rectangle:
    # Class implementation here

    @classmethod
    def to_csv_string(cls, list_objs):
        # Return the CSV string representation of a list of Rectangle instances
