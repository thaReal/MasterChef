#!/usr/bin/python3

# Codeforces - Round 647
# Author: frostD
# Problem D - Johnny and Contribution

from collections import defaultdict 

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	
	
# Definition for an undirected Graph -> this problem is going to need a directed graph (I believe)

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

def find_shortest_path(graph, start, end, path =[]): 
	path = path + [start]
	if start == end:
		return path
	shortest = None
	for node in graph[start]:
		if node not in path:
			newpath = find_shortest_path(graph, node, end, path)
			if newpath:
				if not shortest or len(newpath) < len(shortest):
					shortest = newpath 
	return shortest 


def solve(n, m, references, t):
	graph = Graph(references)
		
	print (graph.print_edges()) #Debug
	print (graph.count_edges()) #Debug
	
	for ti in t:
		pass


# Main
#---
n, m = read_ints()
references = []
for i in range(m):
	a, b = read_ints()
	references.append((a,b))

t = read_ints()

sol = solve(n, m, references, t)
print (sol)
