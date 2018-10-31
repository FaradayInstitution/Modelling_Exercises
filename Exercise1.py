import numpy as np

import matplotlib.pyplot as plt

def myfunc(x):
    return (x**2 + (x-2)**3 -5)

def mybisection(function,a,b,conv):
    while abs(function(a)-function(b)) > conv:
        if np.sign(function(a)) == np.sign(function((a+b)/2)):
            a = (a+b)/2
        if np.sign(function(b)) == np.sign(function((a+b)/2)):
            b = (a+b)/2
    return (a + b) /2

#print(mybisection(myfunc,1,3,0.0001))

#x = list(np.linspace(0,4,100))
#data = []
#for i in x:
#    data.append(myfunc(i))

def myfunc2(x):
    return np.sin(x**2)- x + 5

#print(mybisection(myfunc2,3.8,6,0.001))
#print(mybisection(myfunc2,3.8,5.5,0.001))

x1 = list(np.linspace(3.8,6,100))
data1 = []
for i in x1:
    data1.append(myfunc2(i))

#plt.plot(x1,data1)
#plt.show()


def myfunc3(x):
    return (x-2)**2

#print(mybisection(myfunc3,0,3,0.001))


#x2 = list(np.linspace(0,3,100))
#data2 = []
#for i in x2:
#    data2.append(myfunc3(i))

#plt.plot(x2,data2)
#plt.show()

def myfunc4(x):
    return np.tan(x)

#print(mybisection(myfunc4,1,2,0.001))


x3 = list(np.linspace(1,2,100))
data3 = []
for i in x3:
    data3.append(myfunc4(i))

plt.plot(x3,data3)
plt.show()


