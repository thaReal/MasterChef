#!/usr/bin/python3

# Codeforces - Round 645
# Author: frostD
# Problem B - Maria Breaks the Self-Isolation

from collections import Counter

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, a):
	cntr = Counter(a)
	glist = list(cntr.keys())
	glist.sort()
	grannies = 1
	
	gacc = 0
	for i in range(len(glist)):
		gmin = glist[i]
		ngrannies = cntr[gmin] + grannies + gacc
		if ngrannies > gmin:
			grannies += cntr[gmin] + gacc
			gacc = 0
		else:
			gacc += cntr[gmin]
	
	
	return grannies


# Main
t = read_int()
for case in range(t):
	n = read_int()
	a = read_ints()
	sol = solve(n, a)
	
	print (sol)
