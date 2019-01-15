#!/usr/bin/env python
# coding: utf-8

# In[2]:


from scipy import interpolate
import matplotlib.pyplot as plt
from sympy import polys,Symbol,poly
from numpy import poly1d
import numpy as np


# In[5]:


def CubicSpline(X,Y):
    """ Overall description
        -------------------
        This method will calculate the cubic spline for every point (xi, yi) for i in [0...n-1]
        where n is the number of given points.
        This method creates two objects:
        1. general spline function spline_val that will calculate for any x in [x0, xn-1] the approximation to
        f(x) where f is the 'original' function.
        2. An array cs which contains all the calculated cubic splines for interval [xi, xi+1] in X.
        
        Parameters
        ----------
        1. X - float array
            The x coordinates of the given points.
        2. Y - float array
            The y coordinates of the given points.
            
        Return
        ------
        1. spline_val - function
            A function which takes a float and returns the spline approximation of the given value.
        2. cs_array - polynomial array
            An array which contains all the cubic splines.
    
    """
    def generateSplines(X,Y):
        sx = interpolate.CubicSpline(X, Y)
        s=[] # generating the coefficients of the bspline
        for i in range(0,len(X)-1):
            s.append(createPoly(x[i],[sx.c[3,i],sx.c[2,i],sx.c[1,i],sx.c[0,i]]))
            #Create polynomials for each [x[i],x[i+1]] using the bspline coefficients
        return s
    
    def spline_val(X):
        return interpolate.splev(X, cs_array)
        # splev() to actually evaluate the spline at the desired point.
        
    def createPoly(w, y):
        
        # Create polynomials bspline coefficients
        x = Symbol('x')  # using x to represent 'x' in the expression
        pol = polys.polytools.poly_from_expr(y[0] + y[1] * (x - w) + y[2] * (x - w) ** 2 + y[3] * (x - w) ** 3)
        # Creating a Poly object using expression
        pol = poly1d(pol[0].all_coeffs())
        # Creating poly1 object from the Poly object with its coefficients
        return pol
    
    s=generateSplines(X,Y) # generating splines in String form
    cs_array = interpolate.splrep(X, Y,k=3)
    # the coefficients describing the spline (of 3rd degree) curve are computed,using splrep().
    # splrep returns an array of tuples containing the coefficients.
    return spline_val,s #returning the f(x) function that was calculated


# In[7]:


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


# In[8]:


x=[0.3,0.4,0.5,0.6,0.7,0.8,0.9]
y=[13.7241,13.9776,14.0625,13.9776,13.7241,13.3056,12.7281]
cs,s=CubicSpline(x,y)
for i in range(len(s)):
    print("{0}<=x<={1} , S{2}(x):\n{3}".format(x[i],x[i+1],i,poly_to_string(s[i])))
print("value of S(0.65): {}".format(cs(0.65)))


