# import os

# # This function takes two arguments, a and b, and returns their sum
# def sum_of_two_numbers(a, b):
#     # Return the sum of a and b
#     return a + b

# # Call the function with arguments 1 and 2, and print the result
# print(sum_of_two_numbers(1, 2))

# # what is recursion code
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#     # Testing the factorial function with different values of n and printing the results to the console.
# print("Factorial of 5 is ", factorial(5))



# what is the code of fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
    # Testing the factorial function with different values of n and printing the results to the console.
    n = 8
    print(fibonacci(n))


# fibonacci code
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
    # Testing the factorial function with different values of n and printing the results to the console.
    for i in range(1,11):
        print(fibonacci(i))
        
        
        

print("Hello Aamir")
