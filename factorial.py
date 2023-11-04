##### Recursive approach
def factorial(n):
    return 1 if (n == 1 or n ==0 ) else n * factorial(n -1)

n = 5
print(f"factorial of {n} is {factorial(n)}")


##### Iterative approach
def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n 
            n -= 1
        return fact
n = 5
num = factorial(n)
print(f"factorial of {n} is {num}")


def factorial(n):
    res = 1
    for i in range(2, n+1):
        res *= i 
    return res
n = 5
num = factorial(n)
print(f"factorial of {n} is {num}")


#### Using built in module 
import math
def factorial(n):
    return(math.factorial(n))
n = 5
num = factorial(n)
print(f"factorial of {n} is {num}")


##### using numpy method
import numpy
n = 5
x = numpy.prod([i for i in range(1, n+1)])
print(x)



