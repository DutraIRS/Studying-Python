def feed_cat(name, food):
    return "{cat} is happily eating {food}".format(cat=name, food=food)

def factorial(number):
    if number < 0:
        raise ValueError("Number must be non-negative")
    
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result

# Equivalence Partitioning
# One test for each partition

def is_positive(number):
    return number > 0

test_values = [-1, 0, 1]

for value in test_values:
    result = is_positive(value)

    if result:
        print("{value} is positive".format(value=value))
    else:
        print("{value} is not positive".format(value=value))

# Boundary Value Analysis

import math

def calculate_sqrt(number):
    if number < 0:
        raise ValueError("Number must be non-negative")

    return math.sqrt(number)

valid_inputs = [0, 1, 100]
invalid_inputs = [-1, -100]

for value in valid_inputs + invalid_inputs:
    try:
        result = calculate_sqrt(value)
        print("The square root of {value} is {result}".format(value=value, result=result))
    except ValueError as error:
        print(error)
        print("Invalid input: {value}".format(value=value))

# Input Validation
