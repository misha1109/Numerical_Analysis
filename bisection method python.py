#!/usr/bin/env python
# coding: utf-8

# In[6]:
import math
import numpy

def bisection_method(func, lower, upper, tolerence, max_iterations, real_root = None):
    """ Overall description:
        --------------------
        Bisection method - an iterative method to find a root in an interval of function f
        if and only if f is a continuous function and f(a), f(b) are of opposite signs,
        meaning to approximate a solution of the equation f(x) = 0 in the interval [a,b]. 
        
        Parameters:
        -----------
        func - the function for which we are trying to approximate a solution f(x)=0.
        lower, upper - real numbers, the interval in which to search for a solution.
        tolerance - real number, the maximum error accepted.
        max_iterations - positive integer, the maximum number of iterations the method will perform.
        real_root - real number(optional), for comparison purposes only, does not affect the method. 
        
        Output/Return:
        --------------
        c - the midpoint of the Nth interval computed by the bisection method.
        If both the initial f(a) and f(b) are of the same sign then the method will fail
        The function will also print the current iteration and he difference from the real root
        if it is provided.
    """
    if func(lower) * func(upper) > 0:
        print("Bisection method will fail.")
    else:
        mid = (lower + upper) / 2.0
        iterations = 0
        while (upper - lower) / 2.0 > tolerence and iterations <= max_iterations:
            current_iteration_print = "Iteration: {0},".format(iterations) 
            if func(mid) == 0:
                return c
            elif func(lower) * func(mid) < 0:
                upper = mid
            else:
                lower = mid
            mid = (lower + upper) / 2.0
            current_iteration_print += " Current root approximation: {0},".format(mid)
            if real_root != None:
                current_iteration_print += " Difference from the real root: {0}".format(abs(real_root - mid))
            print(current_iteration_print)
            iterations = iterations + 1
        if real_root != None:
            print("Final approximation: {0}, Difference from the real root: {1}".format(mid, abs(real_root - mid)))
        else:
            print("Final approximation: {0}".format(mid))
        return mid


# # In[2]:
#
#
# def f1(x):
#     return x + 1
#
#
# # In[3]:
#
#
# def f2(x):
#     return x**3
#
#
# # In[7]:
#
#
# bisection_method(f1, -2.6, -0.1, 0.01, 30, 0)
#
#
# # In[9]:
#
#
# bisection_method(f2, -0.4, 2, 0.0001, 30, 0)


def g(x):
    return numpy.log(x)-((x+1)/(x-1))

print(bisection_method(g, 0.1, 0.99, 0.001, 20, 0))
print(bisection_method(g, 3, 5, 0.001, 20,0))

