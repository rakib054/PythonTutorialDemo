# Lambda function is anonymous function which can be used in a line anywhere without defining a function , even in variable

double = lambda x : x * 2
triple = lambda x : x * 3
square = lambda x : x * x 
cube = lambda x : x * x * x
average = lambda x , y : (x + y)/2
power = lambda value , pow : value ** pow

print("Double of 5 is :", double(5))
print("Triple of 5 is :", triple(5))
print("Square of 5 is :", square(5))
print("Cube of 5 is :", cube(5))
print("Average of 5 is :", average(4, 6))
print("5th Power of 5 is :", power(5, 5))


### Using lambda function in Function

def appl(fx , value):
    return 6 + fx(value)

print(appl(lambda x : x * 3 , 5))


### More Example :
def operate_on_numbers(operation, x, y):
    return operation(x, y)

# Example usage with lambda functions
addition = lambda a, b: a + b
subtraction = lambda a, b: a - b
multiplication = lambda a, b: a * b

result1 = operate_on_numbers(addition, 5, 3)
print("Result of addition:", result1)

result2 = operate_on_numbers(subtraction, 5, 3)
print("Result of subtraction:", result2)

result3 = operate_on_numbers(multiplication, 5, 3)
print("Result of multiplication:", result3)

# A good example indeed
print(operate_on_numbers(lambda a, b: ((a + (a * b)) -b), 5 , 3))


### MORE EXAMPLE ........
def apply_operation_to_list(operation, numbers):
    return [operation(num) for num in numbers]

# Example usage with lambda functions using list
numbers = [1, 2, 3, 4, 5]

print("Original Numbers:", numbers)
print("Squared Numbers:", apply_operation_to_list(lambda x: x**2 , numbers))
print("Cubed Numbers:", apply_operation_to_list(lambda x: x**3
 , numbers))
print("Doubled Numbers:", apply_operation_to_list(lambda x: x * 2 , numbers))