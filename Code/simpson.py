# Numerical Integral

## Guide ##
# a => upper limit of integral
# b => lower limit of integral
# n => number of subdivisions
# f => equation

import numpy as np

# Simpson Method
def simpson(a,b,n,f):
    
    result = 0
    h = (a-b) / n
    
    i = 0
    while(i<=n+1):
        x0 = b + i*h
        i += 1
        x1 = b + i*h
        i += 1
        x2 = b + i*h
        if (x2>=a):
            x2 = a
            
        k = h*(f(x0) + 4 * f(x1) + f(x2))/3
        result += k
    
    return result