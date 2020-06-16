#!/usr/bin/python3

# Codeforces - Round 650
# Author: frostD
# Problem A - Short Substrings


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(b):
	a = b[:2]
	for i in range(3, len(b), 2):
		a += b[i]
	return a


# Main
t = read_int()
for case in range(t):
	b = input()
	sol = solve(b)
	print (sol)
