#!/usr/bin/python3

# Codeforces - Round 655
# Author: frostD
# Problem A - Omkar and Completion


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve():
	sol = [1, 1]
	while len(sol) < 1000:
		i = sol[-1] + 2
		sol.append(i)
		sol.append(i)
	
	sol_str = [str(x) for x in sol]
	return sol_str


# Main
t = read_int()
arr = solve()
for case in range(t):
	n = read_int()
	sol = arr[:n]
	print (' '.join(sol))
