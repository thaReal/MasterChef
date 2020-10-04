#!/usr/bin/python3

# Codeforces - Round #675
# Author: frostD
# Problem A - Fence

from math import sqrt, floor

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(a, b, c):
	d = (a+b+c) - 1
	return d
	

# Main
t = read_int()
for case in range(t):
	a, b, c = read_ints()
	sol = solve(a, b, c)
	print (sol)
