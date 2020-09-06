#!/usr/bin/python3

# Codeforces - Round 668
# Author: frostD
# Problem A - Permutation Forgery


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, p):
	return ' '.join([str(x) for x in p[::-1]])


# Main
t = read_int()
for case in range(t):
	n = read_int()
	p = read_ints()
	
	sol = solve(n, p)
	
	print (sol)
