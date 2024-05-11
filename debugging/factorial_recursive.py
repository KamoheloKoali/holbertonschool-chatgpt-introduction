#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculates the factorial of a non-negative integer n.

    Parameters:
    - n (int): The non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the input integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the input from command-line arguments and calculate the factorial
f = factorial(int(sys.argv[1]))

# Print the calculated factorial
print(f)

