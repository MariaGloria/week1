from __future__ import division
import numpy as np
def ex3(a,b,m,nmax):
    I=0.0
    dx=(b-a)/nmax
    
    for i in range (0,nmax):
        I+=np.sin(m*(a+(i+0.5)*dx))
    I*=dx
    exact=-np.cos(m*b)*1/m + np.cos(m*a)*1/m
    print (I, '\Exact integral=',exact,',error=',I-exact)
    e=I-exact
    return (I,dx,e)

array=[4000,40000,400000,4000000]
dxs=[]
es=[]
ns=np.empty(3)
for interv in array:
    I,dx,e= ex3(0,np.pi,3,interv)
    
    dxs.append(dx)
    es.append(e)
    
plt.plot(dxs,es)

for j in range(0,3):
    ns[j]=(np.log(es[j])-np.log(es[j+1]))/(np.log(dxs[j])-np.log(dxs[j+1]))



