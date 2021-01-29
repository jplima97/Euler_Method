import numpy as np
import matplotlib.pyplot as plt
import math

'''
It is possible to notice that for cases h = 5 and h = 1, the lower the value,
   closer to the exact solution the methods come closer.
'''
# Defining global parameters ===============================================
N0 = 1000
L = 0.1 # Lambda
h = 1
t0 = 0
tf = 50
n = int((tf-t0)/h)

# Explicit Euler method =================================================
x1 = []
y1 = []
for i in range(n+1):
    t = t0 
    t0 = t0 + h
    N = N0
    N0 = N0 + (-L*N)*h
    x1.append(t)
    y1.append(N)
array_x1 = np.array(x1)
array_y1 = np.array(y1)

# Implicit Euler method ==================================================
N0 = 1000
t0 = 0
tf = 50

x2 = []
y2 = []
for i in range(n+1):
    t = t0 
    t0 = t0 + h
    N = N0
    N0 = N0/(1 + L*h)
    x2.append(t)
    y2.append(N)
array_x2 = np.array(x2)
array_y2 = np.array(y2)

# Exact solution ==============================================================
N0 = 1000
t0 = 0
tf = 50

x3 = []
y3 = []
for i in range(n+1):
    t = t0 
    t0 = t0 + h
    N = N0*math.exp(-0.1*t)
    x3.append(t)
    y3.append(N)
array_x3 = np.array(x3)
array_y3 = np.array(y3)

# Plotting the images =======================================================
plt.plot(array_x1,array_y1,color='red',label='Explicit Euler method')
plt.scatter(array_x1,array_y1,c='red',label='Data')

plt.plot(array_x2,array_y2,color='blue',label='Implicit Euler method')
plt.scatter(array_x2,array_y2,c='blue',label='Data')

plt.plot(array_x3,array_y3,color='black',label='Exact solution')
plt.scatter(array_x3,array_y3,c='black',label='Data')

plt.xlabel('Time')
plt.ylabel('Númber of atoms')
plt.title('h = 1')
plt.legend()
plt.savefig('euler_method_h1.jpeg')
