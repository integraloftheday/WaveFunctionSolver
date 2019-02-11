import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.constants
import scipy.integrate
from TwoOrderEulerandGraph import EulerMethod, Graph, RungeKutta, GraphR
from bisector import hotfix, positiveTorF, selector, mathematicaification
import time 
import csv 

#Function Preperation
#y''=g(t,y,y') can be converted to a first-order system by introducing the variable z to acount for y'
#y'=z
# z'=g(t,y,z) (z'=(y')'=y'')

#E(Intial t value, Intial y value, step, value of approximation, y'=f(t,y,z), z'=g(t,y,z))
#Intial y and z at intial t 
#function utilizes lamaba notation for Defining

#Wave Function: -(ħ^2/2m)*Ψ''(x)+v(x)Ψ(x)=EΨ(x)
#-(ħ^2/2m) = c 
c=-1
E=1

#TODO 
#V(t) needs to be defined ✔
#method for selecting a b for EulerMethod as a function E = EM(E) ✔
#implement bisectionMethod for EM(E) ✔
#Sine and Cosine intial conditions ✔
#reflection across y-axis (optional) ✔
#Normalization function 



#zPrime=lambda t,y,z:(y*2*(E-V(t)))/c
#yPrime=lambda t,y,z:z

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
        pointsV.append((V(x,1)))
        x=x+step
    return(pointsV)

def round2(num):
    return round(num * 2) / 2
def V(x,p): #Infiite Square Wall
    if x>-1 and x<1:
        return 0
    else :
        return 10**3


with open('TrainingInfiteSquareWall.csv', mode='w') as training:
    training = csv.writer(training, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    p=0

    print(p)
    E=[]
    potential=lambda E:RungeKutta(-2,0,.01,.01,2,lambda t,y,z:z,lambda t,y,z:(y*2*(E-V(t,p)))/c)[2][-1] #intervals of [a,b] where f(a)*f(b)<0
    print(potential(0))
    Intervals=selector(.1,.1,12,potential)
    #print(Intervals)
    index=0
    for a,b in Intervals:
        E.append((index,(hotfix(a,b,potential,.1)))) #by passes the slow bisectionmethod function
        index=index+1
    print(mathematicaification(str(E)))

    for i,e in E:
        if e>49:
            print("error")
        else:
            list1=[round2(e)]+[i]+points(V,-4,4,1000)
            training.writerow(list1)
