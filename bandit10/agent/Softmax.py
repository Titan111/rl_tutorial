import math
import random

class Softmax:
	def __init__(self,n,t):
		self.sum_r=[0 for i in range(n)]
		self.count=[0 for i in range(n)]
		self.q=[0 for i in range(n)]
		self.t=t
		self.n=n
	
	def act(self):
		denom = sum(map(lambda x: math.exp(x/self.t),self.q))
		self.q = list(map(lambda x: math.exp(x/self.t)/denom , self.q))

		rnd = random.random()
		sum_prob=0
		for i in range(self.n):
			sum_prob += self.q[i]
			if rnd<sum_prob:
				return i

	def learn(self,action,reward):
		self.count[action]+=1
		self.sum_r[action] += reward
		self.q[action]=self.sum_r[action]/self.count[action]

