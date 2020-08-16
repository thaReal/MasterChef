#!/usr/bin/python3

# Codeforces - Global Round 10
# Author: frostD
# Problem B - Omkar and Infinity Clock


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, k, a):
	if k % 2 == 0:
		m = 2
	else:
		m = 1

	for i in range(m):
		mx = max(a)
		a = [mx - x for x in a]
	
	sol = [str(x) for x in a]
	return sol
	


# Main
t = read_int()
for case in range(t):
	n, k = read_ints()
	a = read_ints()
	
	sol = solve(n, k, a)
	print (" ".join(sol))
