#!/usr/bin/python3

# Codeforces - Round #653 (Div. 3)
# Author: frostD
# Problem A - Required Remainder


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(x, y, n):
	if n % x == y:
		return n
		
	mod = n % x
	if mod > y:
		return n - (mod - y)
		
	k = n - y
	mod = k % x
	return k - (mod - y)
	
		

# Main
t = read_int()
for case in range(t):
	x, y, n = read_ints()
	sol = solve(x, y, n)
	print (sol)
