class Data:
	def __init__(self):
		self.count_hit=0
		self.sum_r=0
		self.r_graph=[]
		self.a_graph=[]
		self.count = 1

	def append(self,a,r):
		if a == True:
			self.count_hit+=1
		self.sum_r +=  r
		self.r_graph.append(self.sum_r/self.count)
		self.a_graph.append(self.count_hit/self.count)
		self.count += 1
