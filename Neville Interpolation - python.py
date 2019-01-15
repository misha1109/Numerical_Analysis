#!/usr/bin/env python
# coding: utf-8

# In[37]:


from sympy import Symbol
from sympy import polys
from numpy import poly1d
import numpy as np
import matplotlib.pyplot as plt


# In[65]:


def neville(datax, datay):
    """
    Finds an interpolated value using Neville's algorithm.
    Returns the Neville's unique polynomial
    Condition: For every i!=j, x[i]!=x[j] and y[i]!=y[j].

    Parameters
    ----------
    x : array_like
        `x` represents the x-coordinates of a set of datapoints.
    y : array_like
        `y` represents the y-coordinates of a set of datapoints, i.e. f(`x`).

    Returns
    -------
    N(x) : function
            Polynomial of degree≤n where n is the number of points in x
    """
    x=Symbol('x')
    n = len(datax)
    poly = n*[0] # Polynomial P[i,j](X)
    iterations = 1
    for k in range(n):
        for i in range(n-k):
            if k == 0: # for 0≤i≤n
                poly[i] = datay[i] #P[i,i](X)=Yi
            else:# for 0≤i<j≤n , j=i+k
                poly[i] = ((x-datax[i+k])*poly[i]+(datax[i]-x)*poly[i+1])#(X-Xj)*P[i,j-1](X)-(X-Xi)*P[i+1,j)(X)
                poly[i] /= (datax[i]-datax[i+k])# /Xi-Xj
        if iterations != 1:
            print("Iteration {}: {} ".format(iterations, poly_to_string(calcPoly(poly[0]))))
        else: 
            print("Iteration {}: {} ".format(iterations, poly[0]))
        iterations = iterations + 1
    print("Final iteration : {} ".format(poly_to_string(calcPoly(poly[0]))))
    return calcPoly((poly[0])) #P[0,n](X)


# In[35]:


def poly_to_string(l):
    polyString = ""
    power = len(l.coefficients) - 1
    for i in l.coefficients:
        if i != 0:
            if power == 0:
                polyString += "{}".format(i)
            else:
                polyString += "({})x^{} + ".format(i, power)
        power -= 1
    return polyString


# In[38]:


def calcPoly(s):
    # creating polynomial from expression
    pol = polys.polytools.poly_from_expr(s)  # construct polynomial from expression
    pol = np.poly1d(pol[0].all_coeffs())  # create poly1d object using coefficients
    return pol


# In[68]:


x=[1, 2, 3, 4]
y=[1, 5, 10, 17]
n=neville(x, y)

def f(x):
    return x ** 2 + 1

t1=np.arange(1, 4, 0.1)
t2=[]
t3=[]
for i in range(len(t1)):
    t2.append(f(t1[i]))
    t3.append(n(t1[i]))
plt.plot(t1,t2,'-r',label='Original f(x)=x^2+1')
plt.plot(t1,t3,'--g',label='Neville polynomial n(x): {}'.format(poly_to_string(n)))
plt.legend(loc='upper left')
plt.show()


# In[25]:


s = Symbol('s')
print((s * 2) / 2)

