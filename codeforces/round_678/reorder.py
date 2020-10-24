#!/usr/bin/python3

# Codeforces - Round #678
# Author: frostD
# Problem A - Reorder


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, m, a):
	sm = 0
	for i in range(n):
		for j in range(i, n):
			sm += (a[j] / (j+1))
	
	# Ugly hack for precision issue
	sm = round(sm)
	if int(sm) == sm:
		if sm == m:
			return "YES"
	
	return "NO"
	

# Main
t = read_int()
for case in range(t):
	n, m = read_ints()
	a = read_ints()
	sol = solve(n, m, a)
	print (sol)
