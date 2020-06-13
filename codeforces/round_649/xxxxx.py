#!/usr/bin/python3

# Codeforces - Round 649
# Author: frostD
# Problem A - XXXXX 


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, x, a):
	if sum(a) % x != 0:
		return n
	
	not_div = [0 for _ in range(n)]
	for i in range(n):
		if a[i] % x != 0:
			not_div[i] = 1
		
	if 1 in not_div:
		return n - min(not_div.index(1), not_div[::-1].index(1)) - 1
	
	
	
	return -1


# Main
t = read_int()
for case in range(t):
	n, x = read_ints()
	a = read_ints()

	sol = solve(n, x, a)
	print (sol)
