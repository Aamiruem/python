import os

# This function takes two arguments, a and b, and returns their sum
def sum_of_two_numbers(a, b):
    # Return the sum of a and b
    return a + b

# Call the function with arguments 1 and 2, and print the result
print(sum_of_two_numbers(1, 2))

# what is recursion code
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
