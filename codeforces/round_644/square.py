#!/usr/bin/python3

# Codeforces - Round 644
# Problem A - Minimal Square


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(a, b):
	min_side = min(a, b) * 2
	max_dim = max(a, b, min_side)
	
	return max_dim**2


# Main
t = read_int()
for case in range(t):
	a, b = read_ints()
	sol = solve(a, b)
	print (sol)
