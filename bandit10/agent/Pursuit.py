import random
import math

class Pursuit:
	def __init__(self,n = 10,a=0.9,b=0.01):
		self.q = [10 for i in range(n)]
		self.pi = [10 for i in range(n)]
		self.n = n
		self.a = a
		self.b = b

	def act(self):
		rnd = random.random()
		sum_prob=0
		for i in range(self.n):
			sum_prob += self.pi[i]
			if rnd<sum_prob:
				return i

	def learn(self,action,reward):
		self.q[action] += self.a*(reward - self.q[action])
		greedy = self.q.index(max(self.q))
		for i in range(self.n):
			target = 0
			if greedy == i:
				target = 1
			self.pi[i] += self.b*(target - self.pi[i])
