import random

class E_Greedy:
	def __init__(self,n,e):
		self.sum_r = [0 for i in range(n)]
		self.count = [0 for i in range(n)]
		self.q = [0 for i in range(n)]
		self.e = e
		self.n = n

	def act(self):
		action = 0
		if random.random() > self.e:
			action = self.q.index(max(self.q))
		else:
			action = random.randint(0,self.n-1)
		return action

	def learn(self,action,reward):
		self.count[action]+=1
		self.sum_r[action] += reward
		self.q[action]=self.sum_r[action]/self.count[action]
