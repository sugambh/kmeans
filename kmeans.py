import random
import math
import matplotlib.pyplot as plt
dataset=[]
centroids=[]
clusters=[]

class Point:#class for specifying points in 2-d
    def __init__(self,a,b):
        self.x=a
        self.y=b
def setpoints(z):#randomly initializing the points
    l=[]
    for i in range(z):
        p=Point(random.uniform(-1,1),random.uniform(-1,1))
        l.append(p)
    return l
def dist(a,b):#calculates the euclidean distance between points
    return math.sqrt(pow(a.x-b.x,2)+pow(a.y-b.y,2))    
def sum(a,b):
    return a.x+b.x,a.y+b.y
n=int(raw_input("enter the number of points\n"))
k=int(raw_input("enter the number of clusters\n"))
iterations=int(raw_input("enter the number of iterations\n"))
dataset=setpoints(n)
centroids=setpoints(k)
s=0
def draw(gole):
    label=[]
    a=[]
    b=[]
    for i in range(len(dataset)):
        a.append(dataset[i].x)
        b.append(dataset[i].y)
        for j in range(len(gole)):
            if i in gole[j]:
                label.append(j)
                break
            else:
                continue


    plt.scatter(a,b,c=label,s=150)
    plt.show()
    plt.close()
print "Press...\n\t1 : to see plot after each iteration\n\t other than 1: for exit\n "
while(s<iterations):
    gole= [[] for i in range(k)]
##
    #assigning each data point to one of the cluster
    for i in range(len(dataset)):
        diff=[]
        for j in range(len(centroids)):
            diff.append(dist(dataset[i],centroids[j]))
            
        val, idx = min((val, idx) for (idx, val) in enumerate(diff))
        gole[idx].append(i)
    line="clusters after "+str(s)+" iteration\n"
    if(int(raw_input(line))==1):
        print "sug"
        draw(gole)
    else:
       break
       

    #updating the centroids with mean of the datapoints in their cluster    
    for i in range(len(centroids)):
        temp=Point(0,0)
        for j in range(len(gole[i])):
            temp.x,temp.y=sum(temp,dataset[gole[i][j]])
        centroids[i].x=temp.x/len(gole[i])
        centroids[i].y=temp.y/len(gole[i])
    s=s+1



