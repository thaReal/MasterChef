#!/usr/bin/python3

# Codeforces - Round 645
# Author: frostD
# Problem A - Park Lighting


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n,m):
	if n*m == 1:
		return 1
	elif n*m % 2 == 0:
		return (n*m) // 2
	else:
		return ((n*m) // 2) + 1


# Main
t = read_int()
for case in range(t):
	n, m = read_ints()
	sol = solve(n,m)
	
	print (sol)
