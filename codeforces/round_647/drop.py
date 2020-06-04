#!/usr/bin/python3

# Codeforces - Round 647
# Author: frostD
# Problem C - Johnny and Another Rating Drop


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n):
	bn = bin(n).count('1')
	return n * 2 - bn
	


# Main
t = read_int()	
for case in range(t):
	n = read_int()
	sol = solve(n)
	print (sol)

