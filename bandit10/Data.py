import numpy as np


class Data:
	def __init__(self):
		self.count_hit=0
		self.sum_r=0
		self.r_graph=[]
		self.a_graph=[]
		self.count = 1

	def add(self,a,r):
		if a == True:
			self.count_hit+=1
		self.sum_r +=  r
		self.r_graph.append(self.sum_r/self.count)
		self.a_graph.append(self.count_hit/self.count)
		self.count += 1

class MultiData:
	def __init__(self,data_n):
		self.data_n=data_n
		self.r_graph=np.zeros(data_n)
		self.a_graph=np.zeros(data_n)
		self.sample_n=0

	def add(self,data):
		self.r_graph += np.array(data.r_graph)
		self.a_graph += np.array(data.a_graph)
		self.sample_n+= 1

	def update(self):
		self.r_graph /= self.sample_n
		self.a_graph /= self.sample_n
