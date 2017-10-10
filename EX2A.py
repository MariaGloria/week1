from __future__ import division
import numpy as np
def ex2a(a,b,m,nmax):
    I=0.0
    dx=(b-a)/nmax
    
    for i in range (0,nmax):
        I+=np.sin(m*(a+(i+0.5)*dx))
    I*=dx
    exact=-np.cos(m*b)*1/m + np.cos(m*a)*1/m
    print (I, '\Exact integral=',exact,',error=',I-exact)
    
ex2a(0,1,1,4)



