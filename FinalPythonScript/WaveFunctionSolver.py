import sys
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.constants
import scipy.integrate

#BISECTOR.py 
def bisectionMethod(a,b,f,tol):
    """bisect method to finding real roots of a continous function f where f(a)*f(b)<0
    tol is the tolarance for the anwser. New test values are computed using m=(a+b)/2"""
    m=0
    while(not(abs(f(m))<=tol)):
        if (f(a)*f(b)>0):
            print("invalid a and b values")
            return("error")
        m=(a+b)/2
        if (f(a)*f(m)<0):
            a=a
            b=m
        else:
            a=b
            b=m
    return m

def hotfix(a,b,f,tol):
    """A hot fix that allows bisectionMethod to be bypassed in favor of the more effiecent selectormethod
    averages the interval the selector provides"""
    return((a+b)/2)
def mathematicaification(word):
    """Makes a list in the format accepted by mathmatica""" 
    for letter in word:
        if(letter=="(" or letter=="["):
            word=word.replace(letter,"{")
        if(letter==")" or letter=="]"):
            word=word.replace(letter,"}")
    return word
def positiveTorF(a):
    """ returns 1 for positve value 
    returns 2 for negative value 
    returns 3 for zero"""
    if a>0:
        return 1 #positve
    elif a<0:
        return 2 #negative
    else:
        return 3 #zero


def selector(minValue,step,numIntervals,f):
    """ Creates a list of of intervals such that [a,b] 
    f(a)*f(b)<0
    minValue: minValue 
    numIntervals: number of Intervals 
    f: function"""
    intervals=[]
    num=minValue
    while(len(intervals)<numIntervals):
        positive=positiveTorF(f(num))
        while(positive==positiveTorF(f(num)) and positiveTorF(f(num))!=0):
            #print(f(num))
            num=num+step
        if positiveTorF(f(num)) != 0:
            intervals.append((num-step,num)) 
            
        else: 
            intervals.append((num-step,num+step))
        num=num+step
        #print(num)
    return intervals

    #TwoOrderEulerandGraph 


#Function Preperation
#y''=g(t,y,y') can be converted to a first-order system by introducing the variable z to acount for y'
#y'=z
# z'=g(t,y,z) (z'=(y')'=y'')

#E(Intial t value, Intial y value, step, value of approximation, y'=f(t,y,z), z'=g(t,y,z))
#Intial y and z at intial t 
#function utilizes lamaba notation for Defining
def square(list1):
    """squares a list of items
    Ex square([1,2,3])=[1,4,9]"""
    return [i ** 1 for i in list1]

def reflection(list1,negativeOrPositive):
    """Reflects list1 about x=0
    negativeOrPositive (-1 or 1) determines if it is also reflected about y=0
    Ex reflection([1,2,3],-1)=[-3,-2,-1,1,2,3]
    Ex reflection([1,2,3],1)=[3,2,1,1,2,3]"""
    reflectedlist=list1
    for x in list1:
        reflectedlist=[negativeOrPositive*x]+reflectedlist
    return reflectedlist

def EulerMethod(initialT,initialY,intialZ,step,approx,yPrime,zPrime):
    """ Method to solve Second order differential equations 
    returns [tValues,zValues,yValues]
    intialT: initial time y(t)=0 the t would be intialT 
    initalY: y(initalT)=IntialY 
    initalZ: y'(initalT)=IntialZ
    step: h 
    approx: max value """
    t=initialT
    y=initialY
    z=intialZ
    tValues=[t]
    yValues=[y]
    zValues=[z]
    while(t<approx):
        
        z=z+step*zPrime(t,y,z)
        
        y=y+step*yPrime(t,y,z)
        t=t+step
        tValues.append(t)
        yValues.append(y)
        zValues.append(z)
        
        
        
    #print((t,z))
    #print((t,y))
    return([tValues,zValues,yValues])

#y'=z 
#z'=y" 
#z=v
#y=x
#@lru_cache(maxsize=1000)
def RungeKutta(initialT,initialY,intialZ,step,approx,yPrime,zPrime):
    t=initialT
    y=initialY
    z=intialZ
    tValues=[t]
    yValues=[y]
    zValues=[z]
    while(t<approx):
        k1=yPrime(t,y,z)*step
        #print("k1 "+str(k1))
        l1=zPrime(t,y,z)*step
        #print("l1 "+str(l1))
        k2=yPrime(t+(step/2),y+(k1/2),z+(l1/2))*step
        #print("k2 "+str(k2))
        l2=zPrime(t+(step/2),y+(k1/2),z+(l1/2))*step
        #print("l2 "+str(l2))
        k3=yPrime(t+(step/2),y+(k2/2),z+(l2/2))*step
        #print("k3 "+str(k3))
        l3=zPrime(t+(step/2),y+(k2/2),z+(l2/2))*step
        #print("l3 "+str(l3))
        k4=yPrime(t+step,y+k3,z+l3)*step
        #print("k4 "+str(k4))
        l4=zPrime(t+step,y+k3,z+l3)*step
        #print("l4 "+str(l4))
        #print("T "+str(t))
        y=y+(k1+2*k2+2*k3+k4)/6
        #print("Y "+str(y))
        z=z+(l1+2*l2+2*l3+l4)/6
        #print("z "+str(z))
        t=t+step
        yValues.append(y)
        zValues.append(z)
        tValues.append(t)
    return([tValues,zValues,yValues])
        


def Graph(initialT,initialY,intialZ,step,maxValue,yPrime,zPrime,reflect,energy,num): #maxValue
    """ Method to solve Second order differential equations 
    displays a graph
    intialT: initial time y(t)=0 the t would be intialT 
    initalY: y(initalT)=IntialY 
    initalZ: y'(initalT)=IntialZ
    step: h 
    maxValue: max value 
    reflect: 0 false -1 reflect negative(sine) 1 reflect positive (cosine)
    """
    tValuesg=[]
    yValuesg=[]
    zValuesg=[]
    points=EulerMethod(initialT,initialY,intialZ,step,maxValue,yPrime,zPrime)
    #print(points[0])
   # print("y")
    #print(points[2])
    #print("z")
    #print(points[1])

    tValuesg=points[0]
    zValuesg=points[1]
    yValuesg=points[2]
    if reflect==-1 or reflect==1: 
        tValuesg=reflection(tValuesg,-1)
        zValuesg=reflection(zValuesg,reflect)
        yValuesg=reflection(yValuesg,reflect)

    yValuesSquared=square(yValuesg)
    plt.figure(1)
    plt.subplot(211)
    plt.plot(tValuesg,yValuesSquared)
    plt.xlabel ('t')
    plt.ylabel('z')
    plt.title("Ψ^2 E="+str(energy))
    plt.subplot(212)
    plt.plot(tValuesg,yValuesg)
    plt.xlabel ('t')
    plt.ylabel('Ψ')
    plt.title("Ψ")
   # plt.savefig("./finiteSquareWellFigures/"+str(num)+".png")
    plt.show()
    plt.close()

def GraphR(initialT,initialY,intialZ,step,maxValue,yPrime,zPrime,reflect,energy,num,p): #maxValue
    """ Method to solve Second order differential equations 
    displays a graph
    intialT: initial time y(t)=0 the t would be intialT 
    initalY: y(initalT)=IntialY 
    initalZ: y'(initalT)=IntialZ
    step: h 
    maxValue: max value 
    reflect: 0 false -1 reflect negative(sine) 1 reflect positive (cosine)
    """
    tValuesg=[]
    yValuesg=[]
    zValuesg=[]
    points=RungeKutta(initialT,initialY,intialZ,step,maxValue,yPrime,zPrime)
    #print(points[0])
    #print("y")
    #print(points[2])
    #print("z")
    #print(points[1])

    tValuesg=points[0]
    zValuesg=points[1]
    yValuesg=points[2]
    if reflect==-1 or reflect==1: 
        tValuesg=reflection(tValuesg,-1)
        zValuesg=reflection(zValuesg,reflect)
        yValuesg=reflection(yValuesg,reflect)

    yValuesSquared=square(yValuesg)
    plt.figure(1)
    plt.subplot(211)
    plt.plot(tValuesg,yValuesSquared)
    plt.xlabel ('t')
    plt.ylabel('z')
    plt.title("Ψ^2 E="+str(energy)+" p="+str(p))
    plt.subplot(212)
    plt.plot(tValuesg,yValuesg)
    plt.xlabel ('t')
    plt.ylabel('Ψ')
    plt.title("Ψ")
    plt.savefig("./powerFigs/"+str(p)+"_"+str(num)+".png")
    plt.show()
    plt.close()

def GraphRS(initialT,initialY,intialZ,step,maxValue,yPrime,zPrime,reflect,energy,num,p): #maxValue
    """ SHOWS THE GRAPH
    Method to solve Second order differential equations 
    displays a graph 
    intialT: initial time y(t)=0 the t would be intialT 
    initalY: y(initalT)=IntialY 
    initalZ: y'(initalT)=IntialZ
    step: h 
    maxValue: max value 
    reflect: 0 false -1 reflect negative(sine) 1 reflect positive (cosine)
    """
    tValuesg=[]
    yValuesg=[]
    zValuesg=[]
    points=RungeKutta(initialT,initialY,intialZ,step,maxValue,yPrime,zPrime)
    #print(points[0])
    #print("y")
    #print(points[2])
    #print("z")
    #print(points[1])

    tValuesg=points[0]
    zValuesg=points[1]
    yValuesg=points[2]
    if reflect==-1 or reflect==1: 
        tValuesg=reflection(tValuesg,-1)
        zValuesg=reflection(zValuesg,reflect)
        yValuesg=reflection(yValuesg,reflect)

    yValuesSquared=square(yValuesg)
    plt.figure(1)
    plt.subplot(211)
    plt.plot(tValuesg,yValuesSquared)
    plt.xlabel ('t')
    plt.ylabel('z')
    plt.title("Ψ^2 E="+str(energy)+" p="+str(p))
    plt.subplot(212)
    plt.plot(tValuesg,yValuesg)
    plt.xlabel ('t')
    plt.ylabel('Ψ')
    plt.title("Ψ")
    plt.savefig("./powerFigs/"+str(p)+"_"+str(num)+".png")
    plt.show()

#MAIN 
#Vars
w=10**3
fx="((1/2)*(x**p))"
a=5
delta=1

print(sys.argv)
w=float(sys.argv[1])
fx=str(sys.argv[2])
a=float(sys.argv[3])
delta=float(sys.argv[4])
print(str(w)+str(type(w)))
print(str(fx)+str(type(fx)))
print(str(a)+str(type(a)))
print(str(delta)+str(type(delta)))

def V(x): #Infiite Square Walls
    if x>-a and x<a:
        return eval(fx)
    else :
        return w


c=-1
p=0

print(p)
E=[]
potential=lambda E:RungeKutta(-(a+delta),0,.01,.01,a+delta,lambda t,y,z:z,lambda t,y,z:(y*1*(E-V(t)))/c)[2][-1] #intervals of [a,b] where f(a)*f(b)<0
#print(potential(0))
Intervals=selector(.01,.01,1,potential)
#print(Intervals)s
index=0
for a,b in Intervals:
    E.append((index,(hotfix(a,b,potential,.1)))) #by passes the slow bisectionmethod function
    index=index+1
print(mathematicaification(str(E)))
