#! /usr/bin/python3
import matplotlib.pyplot as plt
from Bandit10 import bandit10 
from agent import E_Greedy
from agent import Softmax
import Data

ROBOT_N = 3

robot = []
#robot.append(E_Greedy.E_Greedy(10,0.01))
#robot.append(E_Greedy.E_Greedy(10,0.1))
#robot.append(E_Greedy.E_Greedy(10,1))
robot.apped(Softmax.Softmax(10,0.1))
robot.apped(Softmax.Softmax(10,0.01))

log = [Data.Data() for i in range(ROBOT_N)]

for epoch in range(8000):
	for i in range(ROBOT_N):

		action = robot[i].act()
		r=bandit10(action)
		robot[i].learn(action,r)

		hit = True if action == 9 else False
		log[i].append(hit,r)

for i in range(ROBOT_N):
	#plt.plot(log[i].r_graph,label="reward"+str(i))
	plt.plot(log[i].a_graph,label="action"+str(i))

plt.legend()
plt.show()
