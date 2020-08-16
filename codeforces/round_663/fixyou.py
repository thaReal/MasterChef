#!/usr/bin/python3

# Codeforces - Round #663
# Author: frostD
# Problem B - Fix You


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, m, grid):
	# First find C
	for i in range(n):
		for j in range(m):
			if grid[i][j] == 'C':
				cn = i
				cm = j
				break
	
	# DEBUG
	#print ("Cn: {}, Cm: {}".format(cn, cm))

	cntr = 0
	for i in range(n):
		for j in range(m):
			if (i, j) == (cn, cm):
				continue
				
			if i >= cn and grid[i][j] == 'D':
				cntr += 1
				continue
				
			if j >= cm and grid[i][j] == 'R':
				cntr += 1
				continue
				
	return cntr

# Main
t = read_int()
for case in range(t):
	n, m = read_ints()
	grid = []
	for i in range(n):
		grid.append(input())
		
	sol = solve(n, m, grid)
	
	print (sol)
