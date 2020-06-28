#!/usr/bin/python3

from collections import defaultdict

class Graph(object):
	# initialize graph; optional argument edges populates the initial vertex 
	# dictionary with values given as tuples representing connected nodes
	def __init__(self, edges=None): 
		self.V = defaultdict(list)
		self._edge_count = 0

		
		if edges is not None:
			for e in edges:
				self.V[e[0]].append(e[1])
				self.V[e[1]].append(e[0])
				self._edge_count += 1

				
	def add_edge(self, edge):
		self.V[edge[0]].append(edge[1])
		self.V[edge[1]].append(edge[0])
		self._edge_count += 1

		
	def count_edges(self):
		return self._edge_count

		
	def count_verticies(self):
		return len(self.V.keys())

			 
	def print_edges(self):
		edges = list()
		for node in self.V:
			for neighbor in self.V[node]:
				edges.append((node, neighbor))
		
		return edges


def main():
	graph = build_graph()
	edges = []
	for k in graph.V.keys():
		n = len(graph.V[k])
		edges.append(n)
	
	edge_count = {}
	for i in range(50):
		if edges.count(i) != 0:
			edge_count[i] = edges.count(i)
	
	sm = 0
	for i in range(24, 0, -1):
		n = edge_count[i]
		sm += n
		print ("{}: {} - {:0.3f}".format(i, sm, sm/10000.0))
			
	

def build_graph():
	f = open('b1.in', 'r')
	n, m = [int(x) for x in f.readline().split(' ')]
	
	graph = Graph()
	for i in range(m):
		a, b = [int(x) for x in f.readline().split(' ')]
		graph.add_edge((a, b))
	
	f.close()
	
	return graph
	
	
if __name__=='__main__':
	main()
