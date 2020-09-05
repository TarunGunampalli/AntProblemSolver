import random
import math
import matplotlib.pyplot as plt

x = 0
y = 0
trials = 1000
countFell = 0
numSteps = 200
distance = 10
xValues = range(numSteps + 1)
yValues = []

for steps in range(numSteps + 1):
    countFell = 0
    for i in range(trials):
        x = 0
        y = 0
        for iterator in range(steps):
            angle = random.random() * 2 *  math.pi
            x += math.cos(angle)
            y += math.sin(angle)
            if math.sqrt(x**2 + y**2) >= distance:
                countFell += 1
                break
    yValues.append(countFell / trials)
plt.title("numSteps: " + str(numSteps) + "; distance: " + str(distance))
plt.plot(xValues, yValues)
plt.show()
