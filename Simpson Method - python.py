#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import matplotlib.pyplot as plt
from math import fabs
import math


# In[16]:


def simpsonIntegration(f,a,b,n=400000):
    """ Overall description
        -------------------
        Approximate the integral of f(x) from a to b by the Simpson rule
        using the Trapezoid rule and returns T(h ,h / 2)
        where T(h) is the integral using the Trapezoid rule and T(h ,h / 2) is:
        T(f, a, b, n) + 1 / 3 * (T(f , a, b, 2 * n) - T(f ,a ,b , n))
        h = ( b - a) / N
        The higher the N, the better the result will be.

        Parameters
        ----------
        f : function
            Vectorized function of a single variable
        a , b : float numbers
            Interval of integration [a,b]
        N : integer
            Number of subintervals of [a,b]
            default is N=400,000

        Returns
        -------
        float
            Approximation of the integral of f(x) from a to b using the
            Simpsons rule.
    """
    def Trapezoide_method(f,a,b,N=400000, trapz_name = 'h'):
        print("Calculating trapezoide for T({})".format(trapz_name))
        
        x = np.linspace(a,b,N+1) #Intervals through [a,b]
        y = f(x)
        percentage = 10
        dx = (b - a) / N
        sum=y[0]+y[len(y)-1]#f(x[0])+f(x[N])
        for i in range(1,len(y)-1):
            sum+=2*y[i] #[k=1,N-1]Σf(x[k])
            if i % int(N / 10) == 0:
                print("Integral after calculating {}% of the intervals is: {}".format(percentage, sum * dx / 2))
                percentage += 10
        dx = (b - a)/N # Δx
        print("Integral after calculating {}% of the intervals is: {}".format(percentage, sum * dx / 2))
        return(dx/2) * np.sum(sum) #Δx/2*(f(x[0])+[k=1,N-1]Σf(x[k])+f(x[N])
    
    t_h, t_h_2 = Trapezoide_method(f,a,b), Trapezoide_method(f,a,b,2*n,'h/2')
    print("now calculating T(h)+1/3*(T(h/2)-T(h)): {}+1/3*({}-{})={}".format(t_h, t_h_2, t_h,  t_h + 1 / 3 * (t_h_2 - t_h)))
    return t_h + 1 / 3 * (t_h_2 - t_h)


# In[17]:


# def f(x):
#     return 13*pow(x,12)-1.25*pow(x,3)
#
# realVal=1.069932037782943*pow(10,14)
# simpsonsVal=simpsonIntegration(f,3,12)
#
# print("Definite integral of f using the Simpson's rule for [3,12]: {}".format(simpsonsVal))
# print("Real value of the integral: {}".format(realVal))
# print("Error: {}".format(fabs(realVal-simpsonsVal)))
#
# x=np.linspace(3,12,20)
# y=f(x)
# plt.plot(x,y)
# for i in range(20-1):
#     xs = [x[i],x[i],x[i+1],x[i+1]]
#     ys = [0,f(x[i]),f(x[i+1]),0]
#     plt.fill(xs,ys,'b',edgecolor='b',alpha=0.2)
# plt.title('Simpsons Rule, N = {} (N=400,000)'.format(20))
# plt.show()
#
# def f(x):
#    return 2000 * np.log(140000 / (140000 - 2100 * x)) - 9.8 * x
#
# val=simpsonIntegration(f,8,30)
# print("Definite integral of f using the Simpsons rule for range [3,12]: {}".format(val))

exp=np.exp(1)
def f(x):
   return x*math.e**(-x)
valSimps=(simpsonIntegration(f,0,2))
print("Size using Simpsons is: {}".format(valSimps))
