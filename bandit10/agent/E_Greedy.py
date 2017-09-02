from bandit10 import bandit10 
import random

sum_r=[]
for i in range(10):sum_r.append(0);
k=[]
for i in range(10):k.append(0);
q=[]
for i in range(10):q.append(0);
e=0.01


for epoch in range(1000):
	result = 0
	for i in range(100):
		action = 0
		if random.random() > e:
			action = q.index(max(q))
		else:
			action = random.randint(0,9)
		
		k[action]+=1
		r=bandit10(action)
		result += action
		sum_r[action] += r 
		q[action]=sum_r[action]/k[action]
	print(result/100)
print(q)
