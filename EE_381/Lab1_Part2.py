import numpy as np
import matplotlib.pyplot as plt
import random

N = 10000

die = [1,2,3,4,5,6]
results = np.zeros((6,),dtype=int)
print (results)
p1 = 0.1
p2 = 0.15
p3 = 0.3
p4 = 0.25
p5 = 0.05
p6 = 0.15
prob =[p1,p2,p3,p4,p5,p6]
while N > 0:
    choice = random.choices(die, weights = prob)
    #sets the weight of each position from die of being chosen
    
    if choice[0] == die[0]:
        results[0]+=1
        
    if choice[0] == die[1]:
        results[1]+=1

    if choice[0] == die[2]:
        results[2]+=1

    if choice[0] == die[3]:
        results[3]+=1

    if choice[0] == die[4]:
        results[4]+=1

    if choice[0] == die[5]:
        results[5]+=1
    N-=1
print (results)
