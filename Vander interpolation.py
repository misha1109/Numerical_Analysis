#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from numpy.linalg import inv


# ## Vanderize method, gets X and Y and returns a array of the polynom starting from x^0...

# In[9]:


def poly_approx_vandermoode(X, Y):
    """Overall description:
       --------------------
       This is a method to perform polynomial interpolation of the given set of points: X, Y
       The interpolation is done using vander moode matrix.
       
       Parameters:
       -----------
       X,Y - set of points to perform the interpolation on.
       
       Output/Return:
       --------------
       res - the coefficient vector of the polynomial after the interpolation.
       The method will also print out the vector and the polynomial itself.
    """
    matX = np.vander(X, len(X), True)
    invMatX = inv(matX)
    res = np.dot(invMatX, Y)
    print("Polynom: ", end='')
    for i in range(len(res) - 1):
        print("{}x^{} + ".format(res[i], i), end='')
    print("{}x^{}".format(res[len(res)-1], len(res)-1), end='')
    return res


# In[10]:


def vecToFunc(vector):
    """ This function will get a vector an construct a polynomial(function) f(x)
        with each degree having a coefficient from the corrosponding value from
        the vector.
    """
    def f(x):
        f = 0
        for i in range(len(vector)):
            f += vector[i]*x**i
        return f
    return f


# ## Example

# In[16]:


x = [0,1,2]
y = [0,1,4]
t = poly_approx_vandermoode(x,y)
f = vecToFunc(t)
f(4)

