import math
import matplotlib.pyplot as plt
from bandit10 import bandit10 
import random

sum_r=[0 for i in range(10)]
k=[0 for i in range(10)]
q=[0 for i in range(10)]
t=0.05
t2=0.05
r_data = []
a_data = []
for epoch in range(1000):
	ave_reward = 0
	per_hit=0
	N=50
	for i in range(N):
		action = 0
		denominator = sum(map(lambda x: math.exp(x/t2),q))
		probability = list(map(lambda x: math.exp(x/t)/denominator , q))

		rnd = random.random()
		sum_prob=0
		for i in range(len(probability)):
			sum_prob += probability[i]
			if rnd<sum_prob:
				action = i
				break
		
		k[action]+=1
		r=bandit10(action)
		sum_r[action] += r 
		q[action]=sum_r[action]/k[action]

		ave_reward += r
		if action == 9:
			per_hit += 1
	ave_reward/=N
	per_hit/=N
	r_data.append(ave_reward)
	a_data.append(per_hit)
plt.plot(r_data)
plt.plot(a_data)
plt.show()
