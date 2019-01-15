import math
import numpy
def secant_method(func, lower, upper, tolerance, max_iterations, real_root = None):
    """ Overall description:
        --------------------
        Secant method - an iterative method to find a root in an interval of function func
        if and only if func is a continuous function and func(a), func(b) are of opposite signs,
        meaning to approximate a solution of the equation func(x) = 0 in the interval [a,b].
        It is done so by dividing the interval by creating a straight line from the edges of the 
        interval, intersecting the line with the x-axis, changing a to be b and b to be the intersection
        point and repeating the cycle.
        
        Parameters:
        -----------
        func - the function for which we are trying to approximate a solution f(x)=0.
        lower, upper - real numbers, the interval in which to search for a solution.
        tolerance - real number, the maximum error accepted.
        max_iterations - positive integer, the maximum number of iterations the method will perform.
        real_root - real number(optional), for comparison purposes only, does not affect the method.
           
        Output/Return:
        --------------
        next_point - real number, the x intercept of the secant line on the the Nth interval
        given by: next_point = a - f(a)(b - a)/(f(b) - f(a)).
        If f(next_point) == 0 for some intercept next_point then the function returns this solution.
        If all signs of values f(a), f(b) and f(next_point) are the same at any
        iterations, the secant method fails and return None.
    """
    if func(lower) * func(upper) >= 0:
        print("Secant method will fail.")
        return None
    else:
        iterations = 1
        while abs(upper - lower) > tolerance and iterations <= max_iterations:
            current_iteration_print = "Iteration: {0}".format(iterations) 
            next_point = upper - (func(upper) * (upper - lower)) / (func(upper) - func(lower))
            if func(next_point) == 0:
                print(current_iteration_print + "Found exact solution: {0}".format(next_point))
                return next_point
            lower = upper
            upper = next_point
            current_iteration_print += ", Current root approximation: {0}".format(next_point)
            if real_root is not None:
                current_iteration_print += ", Difference from the real root: {0}".format(abs(real_root - next_point))
            iterations = iterations + 1
            print(current_iteration_print)
        
        if real_root is not None:
            print("Final approximation: {0}, Difference from the real root: {1}".format(next_point, abs(real_root - next_point)))
        else:
            print("Final approximation: {0}".format(next_point))
        return next_point




def g(x):
    return numpy.log(x)-((x+1)/(x-1))

print(secant_method(g, 0.1, 0.99, 0.001, 20))
print(secant_method(g, 2, 6, 0.001, 20))
