#!/usr/bin/python3

# Codeforces Round 638
# Author: Daniel Ruland
# Problem A - Phoenix and Balance


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---
def solve(n):
	p1 = []
	p2 = []
	for i in range(1, n+1):
		if i == n:
			p1.append(pow(2,i))
		elif i < n//2:
			p1.append(pow(2,i))
		else:
			p2.append(pow(2,i))
	
	return sum(p1) - sum(p2)
	
# Main
t = read_int()
for case in range(t):
	n = read_int()
	sol = solve(n)
	
	print (sol)
