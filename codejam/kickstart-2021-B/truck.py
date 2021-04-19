#!/usr/bin/python3

'''
Kickstart 2021 - Round B 
Problem: "Truck Delivery"
Author: Daniel Ruland
'''
from collections import defaultdict
import functools
from math import gcd

# Utility Functions
def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

class Graph:
	def __init__(self, n_verticies):
		self.n = n_verticies
		self.V = defaultdict(list)
	
	def add_edge(self, edge):
		self.V[edge[0]].append(edge[1])
		self.V[edge[1]].append(edge[0])
	

# Solution:
def solve(n, q):
	graph = Graph(n)
	costs = dict()
	
	for i in range(n-1):
		x, y, l, a = read_ints()
		graph.add_edge((x, y))
		cost = (max(x, y), min(x, y))
		costs[cost] = [l, a]
	
	sol = []
	for i in range(q):
		c, w = read_ints()
		path = [c]
		while path[-1] != 1:
			edges = graph.V[path[-1]]
			path.append(min(edges))
		
		tolls = []
		for j in range(1, len(path)):
			cost = (path[j-1], path[j])
			l, a = costs[cost]
			
			if w >= l:
				tolls.append(a)
		
		if len(tolls) == 0:
			sol.append(0)
		
		elif len(tolls) == 1:
			sol.append(tolls[0])
		
		else:
			sol.append(functools.reduce(gcd, tolls))
	
	graph.V.destroy()
	costs.destroy()
		
	return ' '.join([str(x) for x in sol])
	
	

# Main
t = read_int()
for i in range(t):
	n, q = read_ints()
	sol = solve(n, q)
	
	# Output
	print ("Case #{}: {}".format(i+1, sol))
