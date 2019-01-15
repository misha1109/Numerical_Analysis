import math
def newton_raphson_method(func, deriv, x, tolerence, max_iterations, real_root = None):
    """ Overall description:
        --------------------
        newton-rapshon method - an iterative method to find a root of function f
        if and only if f is a continuous, derivable function and df(x) != 0 for any x.
        It is done so using the formula: x1 = x0 - f(x0) / df(x0) iteratively.
    
        Parameters:
        -----------
        func - the function.
        deriv - the derivative of the function.
        x - real number, starting estimation of the real root.
        tolerance - real number, the maximum error accepted.
        max_iterations - positive integer, the maximum number of iterations the method will perform.
        real_root - real number(optional), for comparison purposes only, does not affect the method.
        
        Output/Return:
        --------------
        x - real number, the value of the Nth iteration of the formula: x1 = x0 - f(x0) / df(x0).
        (N depends on tolerence and max_iterations)
        If deriv(x) == 0 then the method will fail and will return None
    """
    if deriv(x) == 0:
        print("Newton-Raphson method will fail.")
        return None
    else:
        iterations = 1
        while abs(func(x) / deriv(x)) >= tolerence and iterations <= max_iterations:
            current_iteration_print = "Iteration: {0}".format(iterations)
            if func(x) == 0:
                print(current_iteration_print + "Found exact solution: {0}".format(x))
                return x
            x = x - func(x) / deriv(x)
            if deriv(x) == 0:
                print("Newton-Raphson method will fail.")
                return None
            current_iteration_print += ", Current root approximation: {0}".format(x)
            if real_root is not None:
                current_iteration_print += ", Difference from the real root: {0}".format(abs(real_root - x))
            iterations = iterations + 1
            print(current_iteration_print)
        
        if real_root is not None:
            print("Final approximation: {0}, Difference from the real root: {1}".format(x, abs(real_root - x)))
        else:
            print("Final approximation: {0}".format(x))
        return x


def g(x):
    return math.log(x)-(x+1)/(x-1)
def dg(x):
    return (x**2+1)/x*(x-1)**2

print(newton_raphson_method(g, dg, 0.2, 0.001, 20, 1))
print(newton_raphson_method(g, dg, 1.5, 0.001, 20, 1))