import random 

def bandit10(action):
	if action == 5:
		if 0.8>random.random():
			return 1
		else:
			return 0
	else:
		if 0.2>random.random():
			return 1
		else:
			return 0
		
