import numpy as np
import math

def points(V,minV,maxV,number):
    """V=Potential Function
    minV=min domain value 
    maxV=max domain value 
    number= number of points+1"""
    
    domain=abs(minV)+abs(maxV)
    step=domain/number
    pointsV=[]
    x=minV
    while(x<=maxV):
        pointsV.append((V(x)))
        x=x+step
    return(pointsV)

