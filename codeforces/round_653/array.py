#!/usr/bin/python3

# Codeforces - Round #653 (Div. 3)
# Author: frostD
# Problem D - Zero Remainder Array

from collections import Counter

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, k, a):
	mod_a = [a[i] % k if a[i] >= k else k - a[i] for i in range(n)]
	cntr = Counter(mod_a)
	
	if 0 in cntr.keys():
		cntr.pop(0)
	
	if len(cntr) == 0:
		return 0

	m = max(cntr.values())
	if m == 1:
		return max(cntr.keys()) + 1
	
	k_lst = list(cntr.keys())
	for key in k_lst:
		if cntr[key] != m:
			cntr.pop(key)
	
	offset = max(cntr.keys())
	
	return k * (m - 1) + offset + 1

	


# Main
t = read_int()
for case in range(t):
	n, k = read_ints()
	a = read_ints()
	
	sol = solve(n, k, a)
	print (sol)
