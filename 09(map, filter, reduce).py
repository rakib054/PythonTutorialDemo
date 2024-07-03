import random

# Generate a list of 12 random numbers between 1 and 9
marks = [random.randint(1, 9) for _ in range(12)]
  

### Map

double = lambda x: x * 2
# To directly convert all numbers in any iterable object , Ex: list.
print(map(double, marks))    # Shows map object , so convert it to list
print(" Marks are :", marks)
print("Double are :", list(map(double, marks)))


### Filter

def is_greater_than_five(value):
    return value>5    # Return True if the value is 3 , else return False

print("Numbers greater than 5 is :", list(filter(is_greater_than_five, marks)))


### Reduce
from functools import reduce    # You must import reduce() function from functools.

sum = lambda x, y: x + y
print("The Sum is :", reduce(sum, marks))

# Example:    marks = [8, 2, 5, 7, 3, 1, 9, 6, 4, 9, 5, 3]
# [8, 2, 5, 7, 3, 1, 9, 6, 4, 9, 5, 3]
#   [10, 5, 7, 3, 1, 9, 6, 4, 9, 5, 3]
#      [15, 7, 3, 1, 9, 6, 4, 9, 5, 3]
#         [22, 3, 1, 9, 6, 4, 9, 5, 3]
#            [25, 1, 9, 6, 4, 9, 5, 3]
#              ... ... ... ... ... ...
#                          ... ... ...
#                                   62