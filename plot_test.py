import matplotlib.pyplot as plt
import math

def f(x):
    return math.sin(x ** 0.5) * x;

x = []
y = []
#y2 = []

n = 100

for i in range(n):
    x.append(i / 3.0)
    y.append(f(x[i]))
    #y2.append(math.cos(x[i]))
    
plt.plot(x, y, 'g')
#plt.plot(x, y2, 'r')

plt.axis([min(x), max(x), min(y), max(y)])
plt.show()


