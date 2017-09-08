import random
import math

class Roulette:
	def __init__(self,n):
		self.sum_r = [0.1 for i in range(n)]
		self.count = [1 for i in range(n)]
		self.q = [0.1 for i in range(n)]
		self.n = n

	def act(self):
		denom = math.fsum(self.q)
		rnd = denom * random.random()
		sum_q=0
		for i in range(self.n):
			sum_q += self.q[i]
			if rnd<sum_q:
				return i

	def learn(self,action,reward):
		self.count[action] += 1
		self.sum_r[action] += reward
		self.q[action]=self.sum_r[action]/self.count[action]
