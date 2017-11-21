#! /usr/bin/python3
import random
from Dealer import Dealer

class ActorCritic:
	def __init__(self):
		self.V = [ 0 for i in range(200)]
		self.P = [ 1 for i in range(100)]

	def act(self,x):
		denom = sum(map(lambda x: math.exp(x),self.P))
		prob = list(map(lambda x: math.exp(x)/denom , self.P))

		rnd = random.random()
		sum_prob=0
		for i in range(self.n):
			sum_prob += prob[i]
			if rnd<sum_prob:
			self.old_act = i
				return i

	def learn(self,r):
		self.V[self.old_act]+self.a*()
		

if __name__ == "__main__":
	dealer = Dealer(0.5,50)
	agent = ActorCritic()

	state = dealer.get_hand()
	bet = agent.act(state)
	r = dealer.toss(bet)
	agent.learn(r)

