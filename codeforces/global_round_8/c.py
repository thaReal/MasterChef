#!/usr/bin/python3

# Codeforces - 	Global Round 8
# Author: frostD
# Problem A - C+=


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(a, b, n):
	a, b = min(a,b), max(a,b)
	cntr = 0
	while a <= n and b <= n:
		a, b = b, a+b
		cntr += 1
	
	return cntr


# Main
t = read_int()
for case in range(t):
	a, b, n = read_ints()
	sol = solve(a, b, n)
	print (sol)
