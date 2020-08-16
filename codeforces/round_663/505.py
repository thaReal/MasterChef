#!/usr/bin/python3

# Codeforces - Round 663
# Author: frostD
# Problem D - 505

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, m, matrix):
	pass


# Main
t = read_int()
for case in range(t):
	n, m = read_ints()
	matrix = []
	for i in range(n):
		row = read_ints()
		matrix.append(row)
	
	sol = solve(n, m, matrix)
	
	print (sol)
