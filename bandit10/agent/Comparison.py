import math
import random

class Comparison:
	def __init__(self,n = 10,a = 0.1,b = 0.9):
		self.p=[0.1 for i in range(n)]
		self.reference = math.fsum(self.p)/len(self.p)
		self.n=n
		self.a=a
		self.b=b
	
	def act(self):
		denom = sum(map(lambda x: math.exp(x),self.p))
		prob = list(map(lambda x: math.exp(x)/denom , self.p))

		rnd = random.random()
		sum_prob=0
		for i in range(self.n):
			sum_prob += prob[i]
			if rnd<sum_prob:
				return i

	def learn(self,action,reward):
		diff = reward - self.reference
		self.p[action] += self.b*(diff)
		self.reference += self.a * (diff)
