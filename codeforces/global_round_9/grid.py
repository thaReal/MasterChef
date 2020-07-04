#!/usr/bin/python3

# Codeforces - Global Round 9 
# Author: frostD
# Problem B - Neighbor Grid

from collections import deque

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def check_cell(a, i, j):
	neighbors = 0
	if i > 1:
		if a[i-1][j] > 0:
			neighbors += 1
	if j > 1:
		if a[i][j-1] > 0:
			neighbors += 1
	if i < n-1:
		if a[i+1][j] > 0:
			neighbors += 1
	if j < m-1:
		if a[i][j+1] > 0:
			neighbors += 1
	
	return neighbors

	
	
def inc_neighbors(a, q, i, j, delta):
	if i > 0:
		a[i-1][j] += 1
		delta -= 1
		if check_cell(a, i-1, j) != a[i-1][j]:
			q.append((i-1, j))
			
		if delta == 0:
			return (True, a, q)
	
	if j > 0:
		a[i][j-1] += 1
		delta -= 1
		if check_cell(a, i, j-1) != a[i][j-1]:
			q.append((i, j-1))
			
		if delta == 0:
			return (True, a, q)
	
	if i < n-1:
		a[i+1][j] += 1
		delta -= 1
		if check_cell(a, i+1, j) != a[i+1][j]:
			q.append((i+1, j))
			
		if delta == 0:
			return (True, a, q)
	
	if j < m-1:
		a[i][j+1] += 1
		delta -= 1
		if check_cell(a, i, j+1) != a[i][j+1]:
			q.append((i, j+1))
			
		if delta == 0:
			return (True, a, q)
	
	return (False, a, q)

	


def solve(n, m, a):
	adj = [[True for _ in range(m)] for _ in range(n)]
	for i in range(n):
		for j in range(m):
			if a[i][j] > 0:
				if check_cell(a, i, j) != a[i][j]:
					adj[i][j] = False
	
	q = deque()
	for i in range(n):
		for j in range(m):
			if adj[i][j] == False:
				q.append((i, j))
	
	while len(q) > 0:
		i, j = q.popleft()
		neighbors = check_cell(a, i, j)
		delta = a[i][j] - neighbors
		if delta == 0:
			continue
			
		resp, a, q = inc_neighbors(a, q, i, j, delta)
		if resp == False:
			return "NO"

					
	return a




# Main
t = read_int()
for case in range(t):	
	n, m = read_ints()
	a = []
	for _ in range(n):
		line = read_ints()
		a.append(line)
		
	sol = solve(n, m, a)
	if sol == 'NO':
		print (sol)
	else:
		print ('YES')
		for line in sol:
			print (line)
