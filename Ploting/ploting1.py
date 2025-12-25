import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime 


def slow_feb(x):
    if x <=1 : 
        return x
    else : 
        return slow_feb(x-1)+slow_feb(x-2)


def fast_feb(x):
    if x<=1 :
        return x
    else :
        a,b=0,1

        for i in range(1,x+1):
            a,b=b,a+b

            return a
        

def timeIt(fn,X):
    
    times=[]


    for i in  X:
     st_time=datetime.now()
    
     f=fn(i)
     print(f" fabonachi of {i} is = {f}")

     tim=datetime.now()-st_time
     times.append(tim)

    return times


y=range(1,20)

R=[ i for i in range(20)]
slow=timeIt(slow_feb,R)
fast=timeIt(fast_feb,R)

print(slow)
print(fast)

