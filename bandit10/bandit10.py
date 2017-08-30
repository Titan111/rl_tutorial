import random 

def bandit10(action):
	if action*0.1>random.random():
		return 1
	else:
		return 0
