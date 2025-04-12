"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
def add(a, b): 
    return a+b

def subtract(a, b): 
    return a-b

def multiply(a, b): 
    return a+b

def divide(a, b): 
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")

def logarithm(a, b):
    return math.log(b, a)

def exponent (a,b):
    return a**b
