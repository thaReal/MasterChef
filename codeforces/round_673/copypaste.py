#!/usr/bin/python3

# Codeforces - Round #673
# Author: frostD
# Problem A - Copy Paste


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, k, a):
	a.sort()
	mn = a[0]
	spells = 0
	
	for i in range(1, n):
		while a[i] + mn <= k:
			a[i] += mn
			spells += 1
	
	if a[0] + a[1] <= k:
		spells += 1
		
	return spells 


# Main
t = read_int()
for case in range(t):
	n, k = read_ints()
	a = read_ints()
	sol = solve(n, k, a)
	print (sol)
