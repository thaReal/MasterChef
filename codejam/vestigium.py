#!/usr/bin/python3
'''
Codejam 2020 Qualification Round 
Problem: "Vestigium"
Author: Daniel Ruland
'''

# Utilility Functions
def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

# Main
t = read_int()
case = 1
for x in range(t):
	n = read_int()
	m = []
	for i in range(n):
		m.append(read_ints())
		
	# Solution
	k = 0
	for i in range(n):
		k += m[i][i]
	
	r = 0
	for i in m:
		if len(set(i)) != len(i):
			r += 1
	
	c = 0
	for i in range(n):
		col = []
		for j in range(n):
			col.append(m[j][i])
		
		if len(set(col)) != len(col):
			c += 1
		
	# Output
	print ("Case #{}: {} {} {}".format(x+1, k, r, c))
	case += 1
	
	
