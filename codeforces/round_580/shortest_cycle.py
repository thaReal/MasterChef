#!/usr/bin/python
from collections import defaultdict

class Graph():
	def __init__(self,vertices): 
		self.graph = defaultdict(list)
		self.V = vertices
		
	def addEdge(self,u,v):
		self.graph[u].append(v)
		
	def printGraph(self):
		for k in self.graph.keys():
			print "%s, %s" % (k, self.graph[k])
	
	def isCyclicUtil(self, v, visited, recStack):
		visited[v] = True
		recStack[v] = True
		
		for neighbor in self.graph[v]:
			if visited[neighbor] == False:
				if self.isCyclicUtil(neighbor, visted, recStack):
					return True
				elif recStack[neighbor] == True:
					return True
		
		recStack[v] = False
		return False
	
	def isCyclic(self):
		visited = [False] * self.V
		recStack  = [False] * self.V
		for node in range(self.V):
			if visited[node] == False:
				if self.isCyclicUtil(node, visited, recStack) == True:
					return True
		return False
			
		
# Main
n = int(raw_input())
a = [int(x) for x in raw_input().split(" ")]

g = Graph(n)
for ai in a:
	for aj in a:
		if ai & aj != 0:
			g.addEdge(ai, aj)
			

g.printGraph()
if g.isCyclic() == 1:
	print "Graph is cyclic"
else:
	print "Graph is not cyclic"
