#!/usr/bin/python3

# Codeforces - Round 652
# Author: frostD
# Problem A - FasionabLee


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n):
	if n % 4 == 0:
		return "YES"
		
	return "NO"


# Main
t = read_int()
for case in range(t):
	n = read_int()
	sol = solve(n)
	print (sol)
