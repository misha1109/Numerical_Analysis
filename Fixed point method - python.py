from math import *

def fixed_point_method(func, x, tolerence, max_iterations, real_root = None):
    """ Overall description:
        --------------------
        fixed point method - a method to iterate in the following formula: Xn+1 = f(Xn)
        We first isolate x from the function in order to approximate f(x) = 0 and then iterate
        untill we reached a close enough approximation.
        
        Parameters:
        -----------
        func - the function.
        x - real number, the initial guess.
        tolerance - real number, the maximum error accepted.
        max_iterations - positive integer, the maximum number of iterations the method will perform.
        real_root - real number(optional), for comparison purposes only, does not affect the method.
        
        Output/Return:
        --------------
        x - real number, value of the Nth iteration of the formula: x = f(x)
        N depends on the tolerence and max_iterations.
    """
    if func(x) == x:
        print("Found exact solution: {0}".format(x))
        return x
    else:
        iterations = 1
        while abs(func(x) - x) > tolerence and iterations <= max_iterations:
            current_iteration_print = "Iteration: {0}".format(iterations)
            current_x = func(x)
            if current_x == x:
                print(", Found exact solution: {0}".format(x))
                return x
            else:
                current_iteration_print += ", Current root approximation: {0}".format(current_x)
                if real_root is not None:
                     current_iteration_print += ", Difference from the real root: {0}".format(abs(real_root - current_x))
                iterations = iterations + 1
                print(current_iteration_print)
                x = current_x
            
        if real_root is not None:
            print("Final approximation: {0}, Difference from the real root: {1}".format(current_x, abs(real_root - current_x)))
        else:
            print("Final approximation: {0}".format(current_x))
        return x

def f1(x):
    return sin(x)+(1/2)

def f2(x):
    return (x+10)**(1/4)

print(fixed_point_method(f1, 6, 0.000001, 20))
print(fixed_point_method(f2, 4, 0.001, 20))