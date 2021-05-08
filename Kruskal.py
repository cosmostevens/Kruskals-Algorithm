from Edge import Edge
from Point import Point
# import csv

 
file = open('Input.txt', 'r')
lines = file.readlines()
edges = []
mstEdges = []
points = []
count = 0
for line in lines:
	points.append(Point(count))
	row = line.split('\t')
	for column in range(count, len(row)):
		if int(row[column]) != 0:
			edges.append(Edge(count, column, int(row[column])))
	count += 1

print('\nKruskal\'s Algorithm')
print('\nEdges:')
print('Start\tEnd\tWeight')
for obj in edges:
    print( obj.start, obj.end, obj.weight, sep ='\t' )
edges.sort(key=lambda x: x.weight)

print('\nEdges (Sorted):')
print('Start\tEnd\tWeight')
for obj in edges:
    print( obj.start, obj.end, obj.weight, sep ='\t' )
    

for edge in edges:
	if (not points[edge.start].visited and not points[edge.start].visited):
		points[edge.start].visited = True
		points[edge.end].visited = True
		mstEdges.append(edge)		
print('\nMinimum Spanning Tree Edges:')
print('Start\tEnd\tWeight')
for obj in mstEdges:
    print( obj.start, obj.end, obj.weight, sep ='\t' )
	






