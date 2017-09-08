#! /usr/bin/python3
import matplotlib.pyplot as plt
import random
def printQ(i):
	print("Q["+str(i)+"]="+str(Q[i]))

def r(i):
	return i + random.random()

Q=[1]
a=0.9
printQ(0)
log=[]
for i in range(1,10):
	Q.append(Q[-1]+a*(r(i)-Q[-1]))
	printQ(i)
plt.plot(Q)
plt.show()
