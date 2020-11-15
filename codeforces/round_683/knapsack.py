#!/usr/bin/python3

# Codeforces - Round #683
# Author: frostD
# Problem C - Knapsack 


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---	

def solve(n, W):
	'''new approach; recursive 2D matrix since I don't believe it's possible to solve
	this using a 1D matrix'''
	
	global dp
	dp = [[-1 for x in range(n+1)] for y in range(n+1)]
	
	return dp
	

# Main
t = read_int()
for case in range(t):
	global W
	n, W = read_ints()
	global w
	w = read_ints()
	
	sol = solve(n, W)
	
	print (sol)
