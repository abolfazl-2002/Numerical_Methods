# Numerical Integral

## Guide ##
# a => upper limit of integral
# b => lower limit of integral
# n => number of subdivisions
# f => equation

# Simpson Method

def simpson(a,b,n,f):
    
    result = 0
    h = abs(b - a)/n
    
    i = 0
    while(i<=n):
        x0 = a + i*h
        i += 1
        x1 = a + i*h
        i += 1
        x2 = a + i*h
        if (x2>=b):
            x2 = b
            
        k = h*(f(x0) + 4 * f(x1) + f(x2))/3
        result += k
    
    return result
    
