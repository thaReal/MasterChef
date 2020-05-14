#!/usr/bin/python3

# Codeforces - Round 642
# Problem A - Most Unstable Array


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, m):
	if n <=1:
		return 0
	elif n == 2:
		return m
	else:
		return m * 2
		


# Main
t = read_int()
for case in range(t):
	n, m = read_ints()
	sol = solve(n, m)
	
	print (sol)
