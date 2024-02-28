# Solving 1-unknown equations

## Guide ##
# a => number at the beginning of the period
# b => number at the end of the period
# c => possible answer
# e => error
# f => equation

# Bisection Method
def Bisection(a,b,e,f):
    
    # loop
    while 1==1:
        c = (a + b)/2
        
        # checking the possible answer is correct or no
        if (e<=abs(f(c))):
            if(f(c)*f(a)<0):
                b = c
            else:
                a = c
        else:
            return c
            break
