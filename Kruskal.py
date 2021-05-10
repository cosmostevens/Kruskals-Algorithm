from Edge import Edge

class Kruskal:
	
	parents = []
	levels = []
	edges = []
	points = 0
	
	def buildGraph(self):
		file = open('Input.txt', 'r')
		lines = file.readlines()
		for line in lines:
			row = line.split('\t')
			for column in range(self.points, len(row)):
				if int(row[column]) != 0:
					self.edges.append(Edge(self.points, column, int(row[column])))
			self.points += 1

	def displayEdges(self):
		print('Start\tEnd\tWeight')
		cost = 0
		for edge in self.edges:
			print(edge)
			cost += edge.weight
		print(f'Cost: {cost}')
			
	def findParent(self, index):
		if self.parents[index] == index:
			return index
		return self.findParent(self.parents[index])

	def addParent(self, x, y):
		xParent = self.findParent(x)
		yParent = self.findParent(y)
		if self.levels[xParent] > self.levels[yParent]:
			self.parents[yParent] = xParent
		elif self.levels[xParent] < self.levels[yParent]:
			self.parents[xParent] = yParent
		else:
			self.parents[yParent] = xParent
			self.levels[xParent] += 1

	def kruskalsAlgorithm(self):
		mstEdges = []
		self.edges.sort(key=lambda x: x.weight)
		print('\nEdges (Sorted):')
		self.displayEdges()
		index = 0
		edgeIndex = 0
		for point in range(self.points):
			self.parents.append(point)
			self.levels.append(0)
		while edgeIndex < self.points - 1:
			x = self.findParent(self.edges[index].start)
			y = self.findParent(self.edges[index].end)
			if x != y:
				edgeIndex += 1
				mstEdges.append(Edge(self.edges[index].start, self.edges[index].end, self.edges[index].weight))
				self.addParent(x, y)
			index += 1
		self.edges = mstEdges

	
print('\nKruskal\'s Algorithm')
print('Edges (Before Algorthm):')
kruskal = Kruskal()
kruskal.buildGraph()
kruskal.displayEdges()
kruskal.kruskalsAlgorithm()
print('\nEdges (After Algorthm):')
kruskal.displayEdges()