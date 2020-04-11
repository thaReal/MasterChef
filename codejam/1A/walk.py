#!/usr/bin/python3
'''
Codejam 2020 - Round 1A
Problem: "Pascal Walk"
Author: Daniel Ruland
'''

from math import sqrt


def read_int():
	n = int(input())
	return n
	
	
# dont need any of this, any number can be formed from 
# the first two diagonals

def make_triangle(n):
	tsum = 0
	i = 0
	triangle = list()
	while tsum < n:
		r = i+1
		row = []
		if i+1 == 1:
			row.append(1)
			triangle.append(row)
			tsum += 1
			i += 1
			continue
				
		if i+1 == 2:
			row.append(1)
			row.append(1)
			triangle.append(row)
			tsum += 2
			i += 1
			continue
		
		for k in range(r):
			if k == 0:
				row.append(1)
				tsum += 1
				continue
			
			if k == (r-1):
				row.append(1)
				tsum += 1
				continue
			
			k = triangle[-1][k-1] + triangle[-1][k]
			row.append(k)
			tsum += k
			
		triangle.append(row)
		i += 1
		
		
	return triangle
	
	
		
def solve(N):
	if N == 1:
		r = 1:
	else:
		r = int(sqrt(N)) + 1
	
	
		
	return r


# Main
T = read_int()
for x in range(T):
	# Solution
	N = read_int()
	walk = solve(N)
	
	# Output
	print ("Case #{}:".format(x+1))
	print (walk)
	#for step in walk:
	#	print("{} {}".format(step[0]+1, step[1]+1))
