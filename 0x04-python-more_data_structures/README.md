# Matrix Square Calculator - Python Function README

Welcome to the Matrix Square Calculator! This Python function is designed to help you efficiently compute the square values of integers within a given matrix. Whether you're working with numerical data, performing calculations, or conducting data analysis, this function can be a valuable addition to your toolkit.

## Features

The Matrix Square Calculator function offers the following features:

### Matrix Square Calculation

The function `square_matrix_simple(matrix)` takes a 2-dimensional matrix as input and returns a new matrix. Each element in the new matrix is the square of the corresponding element in the input matrix. The original matrix remains unchanged.

### Simple Integration

Integrating this function into your code is straightforward. You can easily use it within your existing Python scripts to perform matrix square calculations.

## Getting Started

To start using the Matrix Square Calculator function in your projects, follow these steps:

1. Clone the GitHub repository: [alx-higher_level_programming](https://github.com/yourusername/alx-higher_level_programming)
2. Navigate to the `0x04-python-more_data_structures` directory.
3. Import the `square_matrix_simple` function into your Python code using the following syntax:

   ```python
   from 0-square_matrix_simple import square_matrix_simple
   ```

4. Prepare your matrix for calculation. Here's an example of how you might define a matrix:

   ```python
   matrix = [
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]
   ]
   ```

5. Apply the `square_matrix_simple` function to your matrix to calculate the squared values:

   ```python
   new_matrix = square_matrix_simple(matrix)
   ```

6. Print the resulting `new_matrix` and compare it to the original `matrix` to observe the squared values:

   ```python
   print("Original Matrix:")
   print(matrix)

   print("\nNew Matrix (Squared Values):")
   print(new_matrix)
   ```

## Example Usage

Here's an example of how you can use the Matrix Square Calculator function to compute squared values within a matrix:

```python
from 0-square_matrix_simple import square_matrix_simple

# Define the matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Calculate squared values
new_matrix = square_matrix_simple(matrix)

# Print the original and new matrices
print("Original Matrix:")
for row in matrix:
    print(row)

print("\nNew Matrix (Squared Values):")
for row in new_matrix:
    print(row)
```

## Why Use Matrix Square Calculator?

The Matrix Square Calculator function simplifies the process of computing squared values within a matrix. It allows you to perform matrix transformations effortlessly, which can be particularly useful in various data manipulation and analysis tasks. By leveraging this function, you can save time and ensure accurate calculations without modifying the original matrix.

Feel free to experiment with different matrices and explore the results. We hope this function enhances your coding experience and enables you to tackle complex tasks with ease.

Happy coding! íº€
