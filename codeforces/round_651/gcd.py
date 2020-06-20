#!/usr/bin/python3

# Codeforces - Round 651
# Author: frostD
# Problem A - Maximum GCD

from math import gcd

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n):
	if n % 2 == 0:
		return n // 2
	
	return (n - 1) // 2
		


# Main
t = read_int()
for case in range(t):
	n = read_int()
	sol = solve(n)
	print (sol)
