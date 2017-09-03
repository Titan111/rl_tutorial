#! /usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from Bandit10 import bandit10
from agent import E_Greedy
from agent import Softmax
import Data

ROBOT_N = 3
SAMPLE_N = 100
EPOCH_N = 2000
mlog = [Data.MultiData(EPOCH_N) for i in range(ROBOT_N)]

for sample in range(SAMPLE_N):
	robot = []
	robot.append(E_Greedy.E_Greedy(10,0.1))
	robot.append(Softmax.Softmax(10,0.8))
	robot.append(Softmax.Softmax(10,0.5))

	log = [Data.Data() for i in range(ROBOT_N)]

	for epoch in range(EPOCH_N):
		for i in range(ROBOT_N):

			action = robot[i].act()
			r=bandit10(action)
			robot[i].learn(action,r)

			hit = True if action == 9 else False
			log[i].add(hit,r)

	for i in range(ROBOT_N):
		mlog[i].add(log[i])

for i in range(ROBOT_N):
	mlog[i].update()
	#plt.plot(log[i].r_graph,label="reward"+str(i))
	plt.plot(mlog[i].a_graph,label="action"+str(i))

plt.legend()
plt.show()
