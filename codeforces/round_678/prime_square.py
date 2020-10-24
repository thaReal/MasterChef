#!/usr/bin/python3

# Codeforces - Round #678
# Author: frostD
# Problem B - Prime Square


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n):
	ret = [['0' for x in range(n)] for y in range(n)]
	ret[0][0] = '1'
	ret[0][-1] = '1'
	
	for i in range(1, n):
		ret[i][i-1] = '1'
		ret[i][i] = '1'
	
	return ret

	


# Main
t = read_int()
for case in range(t):
	n = read_int()
	sol = solve(n)
	for line in sol:
		print (" ".join(line))
