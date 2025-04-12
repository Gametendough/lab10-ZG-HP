import math

def square_root(a):
    try:
        return math.sqrt(a)  
    except ValueError:
        raise ValueError("Value must be non-negative.")

def hypotenuse(a, b):
    return math.hypot(a, b)

# First example
def add(a, b): 
    return a+b

def subtract(a, b): 
    return a-b


def log(a, b):
    if a<=0 or b<=0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a**b


def mul(a, b): 
    return a+b

def div(a, b): 
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")

