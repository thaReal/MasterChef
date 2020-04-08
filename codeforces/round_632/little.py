#!/usr/bin/python3

# Codeforces - Round 632
# Problem A - Little Artem


# Utilility Functions

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

def solve(n, m):
	sol = []
	val = 'B'
	for i in range(n):
		line = []
		for j in range(m):
			line.append(val)
			val = 'W' if val == 'B' else 'B'
		
		sol.append(line)
		
		if m % 2 == 0:
			val = 'W' if val == 'B' else 'B'
	
	if m*n % 2 == 0:
		sol[0][1] = 'B'

	return sol

# Main
t = read_int()
for case in range(t):
	n, m = read_ints()
	sol = solve(n, m)
	
	for line in sol:
		print (''.join(line))
