# Solving 1-unknown equations

## Guide ##
# a => number at the beginning of the period
# b => number at the end of the period
# c => possible answer
# e => error
# f => equation
# f_ => first derivative of f (eq)

# Newton Method
def Newton(a,b,e,f):
    
    while 1==1:
        c = b - ((f(b) - (b-a))/(f(b)-f(a)))
        f_ = (f(b)-f(c))/(b-c)
        
        # checking the possible answer is correct or no
        if (e<=abs(f(c))):
            if(f_*f(a)>0):
                a = c
            else:
                b = c
        else:
            return c
            break