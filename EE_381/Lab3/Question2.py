import numpy as np
import matplotlib.pyplot as plt


n = 1
counter = 0
points = 3
pie = 2*np.pi
half = 180
np.random.seed()
for i in range(n):
    theta = np.random.uniform(0,pie,points)
    radius = 3#np.random.uniform(0, 5, points) ** 0.5
    print("Theta is " , theta)
    holder = theta[0] + 180
    left = holder - 90
    right = holder + 90
    print("Mid is ", holder)
    print("left is ", left)
    print("right is ", right)
    pt2 = theta[1] + 180
    pt3 = theta[2] + 180
    print("pt2 is " , pt2)
    print("pt3 is " , pt3)
    if(pt2 >= left and pt2 <= right and pt3 >= left and pt3 <= right):
        counter+=1
    #print("X is ", x, " Y is ", y)
    #plt.plot(x,y,'o',color = 'black')
print("Counter is ", counter)
#plt.show()
