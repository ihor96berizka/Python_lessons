import matplotlib.pyplot as plt
import math
import random

#функція активації
def sigmoid(weights, x, y, alp):
    sum = x * weights[0] + y * weights[1] + weights[2]
    return 1.0 / (math.exp(-alp * sum) + 1.0)

#перевірка чи коригувались ваги
def isWeights_updated(data):
    for x in data:
        if not x: return True;
    return False;

#центри першого кластеру
x = []
y = []
#центри другого кластеру
x2 = []
y2 = []

#кількість навчаючих пар
patternCount = 10

#мат. спод та дисперсія першого кластеру
mux = 1
sigma = 0.25
muy = 1

#мат. спод та дисперсія другого кластеру
mux2 = 4
sigma2 = 0.25
muy2 = 2

E0 = 0.1
alp = 1
w = []
output = []
LEARNING_RATE = 0.7
MAX_ITERATION = 1000
modify_weights = []

#згенерувати навчаючі пари і бажаний вихід
for i in range(2 * patternCount):
    if i % 2 == 0:
        x.append(random.gauss(mux, sigma))
        y.append(random.gauss(muy, sigma))
        output.append(0)
    else:
        y.append(random.gauss(muy2, sigma2))
        x.append(random.gauss(mux2, sigma2))
        output.append(1)
    modify_weights.append(False)

#згенерувати ваги
for i in range(3):
    w.append(random.random())

delta = 0
iter_t = 0
#навчання мережі 
while True:
    for it in range(2 * patternCount):
        iter_t += 1
        E = 0

        #порахувати вихід мережі
        OUT = sigmoid(w, x[it], y[it], alp)

        localError = OUT - output[it]

        E = localError ** 2 / 2.0

        if E < E0:
            modify_weights[it] = True

        if E > E0:
            modify_weights[it] = False

            delta = (OUT - output[it]) * OUT * (1.0 - OUT)
            w[0] -= LEARNING_RATE * delta * x[it]
            w[1] -= LEARNING_RATE * delta * y[it]
            w[2] -= LEARNING_RATE * delta
            
    if iter_t >= MAX_ITERATION and not isWeights_updated(modify_weights) : break


for i in range(2 * patternCount):
    if output[i]:
        plt.plot(x[i], y[i], 'ro', label='cluster 1')
    else:
        plt.plot(x[i], y[i], 'go', label='cluster 2')

        
for i in range(3): print(w[i])


x0 = 0.0
xn = 4.3


while x0 < xn:
    yp = -w[0] * x0 / w[1] - w[2] / w[1]
    plt.plot(x0, yp, 'bo', label='separator')
    x0 += 0.1

    
plt.axis([min(x) - sigma, max(x) + sigma, min(y) - sigma, max(y) + sigma])
plt.show()


