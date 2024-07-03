### Recursion of Factorial
def factorial(num):
    if num == 0 or num == 1 :
        return 1
    else:
        return num * factorial(num -1)

# input_Factorial = int(input("Enter the number : "))
# result_Factorial = factorial(input_Factorial)
# print(result_Factorial)


### Recursion of Fibonacci
def fibonacci(num):
    if num == 0:
        return 0
    elif num ==1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

a = int(input("Enter the number : "))
fibonacci_Series = []
for i in range (0,a):
    fibonacci_Series.append(fibonacci(i))

for i in range(len(fibonacci_Series)):
    if i != len(fibonacci_Series) - 1:
        print(fibonacci_Series[i], end=' , ')
    else:
        print(fibonacci_Series[i])
