
import math
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

# TESTS 
#print(bisectionMethod(0,10,lambda t:t**2-3,.001))

#print(selector(0.1,10,lambda x:math.sin(x)))