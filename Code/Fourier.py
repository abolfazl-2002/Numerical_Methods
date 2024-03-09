# Fourier Series Plotter


#%%    IMPORT LIBRARIES    %%#

import numpy as np
import matplotlib.pyplot as plt
from simpson import simpson

#%%   DATA   %%#

f = lambda x : x**3  # Function 
x = np.linspace(-4*np.pi, 4*np.pi,200)  # Domain
n = int(input("Please Enter n: "))  # Number Of Series Element

# Fourier coefficients
a0 = (1/(2*np.pi)) * simpson(np.pi, -np.pi, 200, f)
result = a0*np.ones(200) # Primary Result

#%%   SERIES   %%#

# Loops
for index,j in enumerate(x):
    for i in range(1,n+1):
        
        # Function Combination
        g = lambda w : f(w) * np.cos(i*w)
        z = lambda w : f(w) * np.sin(i*w)
        
        # Fourier coefficients
        an = simpson(np.pi, -np.pi, 500, g)/np.pi
        bn = simpson(np.pi, -np.pi, 500, z)/np.pi
        
        # Update Result
        result[index] += np.cos(i*j)*an + np.sin(i*j)*bn

   
#%%   RESULT   %%#

plt.plot(x,result,lw=1.5)