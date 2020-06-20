#!/usr/bin/python3

# Codeforces - 	Global Round 8
# Author: frostD
# Problem B - Codeforces Subsequences 

from math import factorial

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(k):
	basestr = 'codeforces'
	
	lg = 1
	max_num = factorial(lg)
	while max_num < k:
		lg += 1
		max_num += factorial(lg)
	
	groups = [lg] * lg
	
	
	return groups


# Main
k = read_int()
print (solve(k))
