#!/usr/bin/python3

# Codeforces - Round #643
# Problem B - Young Explorers 

from collections import Counter

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, e):
	groups = 0
	extras = 0
	cntr = Counter(e)
	
	levels = list(cntr.keys())
	levels.sort()
	for l in levels:
		g = cntr[l] // l
		groups += g
		if cntr[l] % l != 0:
			extra = cntr[l] % l
			if extra + extras >= l:
				groups += 1
				extras = extra + extras - l
		
			else:
				extras += extra
		
	return groups		


# Main
t = read_int()
for case in range(t):
	n = read_int()
	e = read_ints()
	sol = solve(n, e)
	
	print (sol)
