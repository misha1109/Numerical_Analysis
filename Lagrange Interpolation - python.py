#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from numpy import poly1d
import matplotlib.pyplot as plt


# In[28]:


def Lagrange_Interpolation(X, Y):
    def poly_to_string(l):
        polyString = ""
        power = len(l.coefficients) - 1
        for i in l.coefficients:
            if i != 0:
                if power == 0:
                    polyString += "{}".format(i)
                else:
                    polyString += "{}x^{} + ".format(i, power)
            power -= 1
        return polyString
    """ Overall description
        -------------------
        The method will return the lagrange interpolating polynomial.
        Given two 1-D arrays `X` and `Y,` which represent the x and y coordinates
        of the point, the method will return the lagrange interpolating polynomial 
        through the points ``(x, y)`` for every (x,y) in X,Y.
        
        No two points will be the same meaning for every i!=j, x[i]!=x[j] and y[i]!=y[j]
        otherwise we will divide by 0.
        The degree of the polynomial will len(x) - 1, e.g if we give 3 point the degree will
        be 2.
        
        Warning: This implementation is numerically unstable. Do not expect to
        be able to use more than about 20 points even if they are chosen optimally.

        Parameters
        ----------
        X : array_like
            X represents the x-coordinates of a set of datapoints.
        Y : array_like
            Y represents the y-coordinates of a set of datapoints, i.e. f(`x`).
            
        Returns
        -------
        polynomial_apporximation : `numpy.poly1d` instance
            The Lagrange interpolating polynomial.
        """
    N = len(X)  # N holds the size of X or the number of points.
    polynomial_apporximation = poly1d(0.0)  # Reset the polynomial approximation to 0.
    for j in range(N):
        lagrange_basis = Y[j] # creating the Lagrange basis polynomial with coefficients y[j]
        for k in range(N):
            if k == j: # If true dont calculate x[j]-x[k] because it equals to zero.(k and j represent the same point)
                continue
            fac = X[j] - X[k] # calculate x[j]-x[k]
            lagrange_basis *= poly1d([1.0, -X[k]]) / fac # calculte (x-x[k])/(x[j]-x[k]) and multiply by it the Lagrange polynomial
        polynomial_apporximation += lagrange_basis # Sum the Lagrange basis polynomial to achieve the Lagrange form
        print("Current iteration i={0}:\n{1}".format(j, poly_to_string(lagrange_basis)))
    print("The final form of the Lagrange polynomial L(x):\n", poly_to_string(polynomial_apporximation))
    return polynomial_apporximation # Return the final form of the polynomial


# In[29]:


x = [1, 2, 3, 4, 5, 6, 7]
y = [-11, -64, 1215, 13312, 70625, 264384, 794731]
l = Lagrange_Interpolation(x, y)


# In[19]:





# In[20]:


def f(x):
    return x ** 7 - 12 * x ** 4


# In[24]:


t1 = np.arange(1, 7, 0.1)
t2 = []
t3 = []
for i in range(len(t1)):
    t2.append(f(t1[i]))
    t3.append(l(t1[i]))
def poly_to_string(l):
    polyString = ""
    power = len(l.coefficients) - 1
    for i in l.coefficients:
        if i != 0:
            if power == 0:
                polyString += "{}".format(i)
            else:
                polyString += "{}x^{} + ".format(i, power)
        power -= 1
    return polyString
print(poly_to_string(l))
    
plt.plot(t1, t2, '-r', label='Original f(x)=x^7-12x^4')
plt.plot(t1, t3, '--g', label='Lagrange polynomial l(x):\n{}'.format(poly_to_string(l)))
plt.legend(loc='upper left')
plt.show()


# In[27]:


help(Lagrange_Interpolation)


x=[0.3,0.4,0.5,0.6,0.7,0.8,0.9]
y=[13.7241,13.9776,14.0625,13.9776,13.7241,13.3056,12.7281]
L=Lagrange_Interpolation(x, y)
print("value of L(0.65): {}".format(L(0.65)))
