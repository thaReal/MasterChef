#!/usr/bin/python3

# Codeforces - Round 648
# Author: frostD
# Problem A - Matrix Game


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, m, matrix):
	sr = set()
	sc = set()
	for i in range(n):
		if 1 not in set(matrix[i]):
			sr.add(i)
	
	for i in range(m):
		col = set()
		for j in range(n):
			col.add(matrix[j][i])
		if 1 not in col:
			sc.add(i)
	
	moves = min(len(sr), len(sc))
	
	if moves % 2 == 0:
		return "Vivek"
	else:
		return "Ashish"
	

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
