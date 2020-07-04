#!/usr/bin/python
from collections import defaultdict 

# --------------------
# Graph Toolbox
# --------------------

# initialize graph; optional argument edges populates the initial vertex 
# dictionary with values given as tuples representing connected nodes
class Graph(object):
	'''Undirected Graph'''
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
		
		
# --------------------

class DirectedGraph(object):
	'''Directed Graph'''
	def __init__(self, edges=None): 
		self.V = defaultdict(list)
		self._edge_count = 0
		
		if edges is not None:
			for e in edges:
				self.V[e[0]].append(e[1])
				self._edge_count += 1
				
	def add_edge(self, edge):
		self.V[edge[0]].append(edge[1])
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




'''
def find_all_paths(graph, start, end, path =[]): 
  path = path + [start] 
  if start == end: 
    return [path] 
  paths = [] 
  for node in graph[start]: 
    if node not in path: 
      newpaths = find_all_paths(graph, node, end, path) 
    for newpath in newpaths: 
      paths.append(newpath) 
  return paths 

  
# function to find the shortest path 
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
          
# Driver function call to print 
# the shortest path 
print(find_shortest_path(graph, 'd', 'c')) 
'''		



# Driver program to the above graph class 
if __name__ == "__main__": 
	graph = Graph() 
	
	graph.add_edge((0, 1))
	graph.add_edge((0, 4))
	graph.add_edge((1, 2))
	graph.add_edge((1, 3))
	graph.add_edge((1, 4))
	graph.add_edge((2, 3))
	graph.add_edge((3, 4))
	
	print graph.print_edges()
	print graph.count_edges()

