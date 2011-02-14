#! /usr/bin/env python

def factorial(x):
    if (x > 1):
        return x * factorial(x - 1)
    else:
        return x

def printFactorial(x):
    print str(factorial(x) )


#printFactorial()
