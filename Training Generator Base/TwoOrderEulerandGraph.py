#Euler's Method For Second Order Differential Equations 

#Dependencies 
import numpy as np
import math
import matplotlib.pyplot as plt
from functools import lru_cache


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
@lru_cache(maxsize=1000)
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
#tested Functions 
#Force spring-mass equation



#GraphR(0,0,0,.1,1.5,lambda t,y,z:yPrime(t,y,z),lambda t,y,z:zPrime(t,y,z),0,0,0)

#GraphR(0,0,0,.5,1.5,lambda t,y,z:z,lambda t,y,z:4*math.sin((3*math.pi*t)/2)-16*y,0,0,0)
#predator Prey Equation
