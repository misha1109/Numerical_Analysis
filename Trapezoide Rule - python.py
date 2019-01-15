import math
#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib.pyplot as plt
from math import fabs


# In[13]:


def Trapezoide_method(f,a,b,N=400000, trapz_name = 'h'):
    """ Overall description
        --------------------
        Approximate the integral of f(x) from a to b by the trapezoid rule.
        The trapezoid rule approximates the integral ∫f(x)dx from a to b by the sum:
        (dx/2)*(f(x[0])+[k=1,N-1]Σf(x[k])+f(x[N])
        where dx = (b - a)/N.
        The Higher the N value is, the better result.

        Parameters
        ----------
        f - function
            Vectorized function of a single variable
        a , b : float numbers
            Interval of integration [a,b]
        N : integer
            Number of subintervals of [a,b]

        Returns
        -------
        float
            Approximation of the integral of f(x) from a to b using the
            trapezoid rule with N subintervals of equal length.

    """
    print("Calculating trapezoide for T({})".format(trapz_name))
    x = np.linspace(a, b, N + 1)
    y = f(x)
    dx = (b - a) / N  # Δx
    percentage = 10
    sum = y[0]+y[len(y)-1] #f(x[0])+f(x[N])
    for i in range(1,len(y)-1):
        sum += 2 * y[i] #[k=1,N-1]Σf(x[k])
        if i % int(N / 10) == 0:
            print("Approximation of the integral after calculating {}% of the intervals is: {}".format(percentage, sum * dx / 2))
            percentage += 10
    print("Approximation of the integral after calculating {}% of the intervals is: {}".format(percentage, sum * dx / 2))
    return (dx / 2) * np.sum(sum) #Δx/2*(f(x[0])+[k=1,N-1]Σf(x[k])+f(x[N])


# In[14]:


# def f(x):
#     return 13 * (x ** 12 ) - 1.25 * (x ** 3)
#
# # print("The sum is {}".format(Trapezoide_method(f, 0, 1)))
#
# realVal=1.069932037782943*pow(10,14)
# val=Trapezoide_method(f,3,12)
#
# print("Definite integral of f using the Simpson's rule for [3,12]: {}".format(val))
# print("Real value of the integral: {}".format(realVal))
# print("Error: {}".format(fabs(realVal-val)))

#
# x=np.linspace(3,12,20)
# y=f(x)
#
# plt.plot(x,y)
# for i in range(20-1):
#     xs = [x[i],x[i],x[i+1],x[i+1]]
#     ys = [0,f(x[i]),f(x[i+1]),0]
#     plt.fill(xs,ys,'b',edgecolor='b',alpha=0.2)
# plt.title('Trapezoid Rule, N = {}'.format(20))
# plt.show()


def f(x):
   return 2000 * np.log(140000 / (140000 - 2100 * x)) - 9.8 * x
#
# val=Trapezoide_method(f,8,30)
# print("Definite integral of f using the Trapezoide rule for range [3,12]: {}".format(val))


def f(x):
   return 2000 * np.log(140000 / (140000 - 2100 * x)) - 9.8 * x
realVal=11061.33553508099
n=30500
valTrapez=(Trapezoide_method(f,8,30,n))
print("Size using Trapezoid is : {}".format(valTrapez))
print("With {} itterations the size of the error is lower than 10**-6".format(n))