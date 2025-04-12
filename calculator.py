"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

<<<<<<< HEAD
def square_root(a):
    try:
        return math.sqrt(a)  
    except ValueError:
        raise ValueError("Value must be non-negative.")

def hypotenuse(a, b):
    return math.hypot(a, b)

=======
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a==0:
        raise ZeroDivisionError
    return b / a
=======
>>>>>>> e61cc3eea5f428ce28e979d69fc442472702abd3
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


def multiply(a, b): 
    return a+b

<<<<<<< HEAD
def divide(a, b): 
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")

=======
>>>>>>> e61cc3eea5f428ce28e979d69fc442472702abd3
def logarithm(a, b):
    return math.log(b, a)

def exponent (a,b):
    return a**b
