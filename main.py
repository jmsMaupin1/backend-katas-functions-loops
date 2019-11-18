#!/usr/bin/env python
"""Implements math functions without using operators except for '+' """

__author__ = "James Maupin"

from functools import reduce

def add(x, y):
    """Add two integers. Handles negative values."""
    return x + y


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    return x * y


def power(x, n):
    """Raise x to power n, where n >= 0"""
    return x ** n


def factorial(x):
    """Compute factorial of x, where x > 0"""
    if x == 0: return 1
    return reduce(lambda x, y: x * y, [i for i in range(x, 0, -1)])

def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    fib = [0, 1, 1, 2]
    if n < len(fib):
        return fib[n]

    return fibonacci(n-1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(factorial(3))
    pass
