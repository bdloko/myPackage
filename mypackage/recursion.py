import numpy as np

def sum_array(array):
    s = 0
    for i in array:
        s += i
    return s

    #Return sum of all items in array

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

    '''Return nth term in fibonacci sequence'''

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

    #Return n!'''

def reverse(word):
    return word[::-1]

    #Return word in reverse'''