class Edge:
	def __init__(self, start, end, weight):
		self.start = start
		self.end = end
		self.weight = weight

	def __str__(self):
		return '{self.start}\t{self.end}\t{self.weight}'.format(self=self)