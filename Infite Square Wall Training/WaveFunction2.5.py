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
def V(x,p): #Infiite Square Wall
    if x>-6 and x<6:
        return p
    else :
        return 10**3

def VP(x,p): #Infiite Square Wall
    if x>-6 and x<6:
        return p
    else :
        return 0
def points(minV,maxV,number):
    """V=Potential Function
    minV=min domain value 
    maxV=max domain value 
    number= number of points+1"""
    
    domain=abs(minV)+abs(maxV)
    step=domain/number
    pointsV=[]
    x=minV
    while(x<=maxV):
        pointsV.append((VP(x,p)))
        x=x+step
    return(pointsV)

def round2(num):
    return round(num * 2) / 2


with open('TrainingInfiteSquareWall.csv', mode='w') as training:
    training = csv.writer(training, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    p=0
    while(p<300):
        if(p%10<.0001):
            print(p)
        #print(p)
        #print(p)
        E=[]
        potential=lambda E:RungeKutta(-5,0,.01,.01,5,lambda t,y,z:z,lambda t,y,z:(y*(E-V(t,p)))/c)[2][-1] #intervals of [a,b] where f(a)*f(b)<0
        #print(potential(0))
        Intervals=selector(.01,.01,1,potential)
        #print(Intervals)
        index=0
        for a,b in Intervals:
            E.append((index,(hotfix(a,b,potential,.1)))) #by passes the slow bisectionmethod function
            index=index+1
        #print(mathematicaification(str(E)))
        print((p,E[0][1]))
        for i,e in E:
            list1=[int(str(e)[0])]+[i]+points(-4,4,1000)
            training.writerow(list1)
        p=p+.05
