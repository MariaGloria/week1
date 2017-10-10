from __future__ import division
def ex2a(a,b,nmax=4):
    I=0.0
    dx=(b-a)/nmax
    
    for i in range (0,nmax):
        I+=3*(a+(i+1/2)*dx)-2
    I*=dx
    print I