import csv
def V(x,p): #Infiite Square Wall
    if x>=-5 and x<=5:
        return p
    else :
        return 10**3
def points(t,minV,maxV,number):
    """V=Potential Function
    minV=min domain value 
    maxV=max domain value 
    number= number of points+1"""
    
    domain=abs(minV)+abs(maxV)
    step=domain/number
    pointsV=[]
    x=minV
    while(x<=maxV):
        pointsV.append((V(x,t)))
        x=x+step
    return(pointsV)


with open('2L.csv', mode='w',newline='') as training:
    training = csv.writer(training, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

      #training = csv.writer(training, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    t=0
    while(t<1010):
        E=t+.095
        #print(int(str(E)[0]))
        list1=[int(str(E*10000)[0:2])]+points(t,-5,5,50)
        #print(list1)
        #print(len(list1))
        training.writerow(list1)
        t=t+.01
   
    