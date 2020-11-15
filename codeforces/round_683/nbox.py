#!/usr/bin/python3

# Codeforces - Round #683
# Author: frostD
# Problem B - Numbers Box 


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, m, a):
	ncount = 0
	total = 0
	gmin = None
	zero = False
	
	for i in range(n):
		row = a[i]
		if 0 in row:
			zero = True
		
		for val in row:
			if val < 0:
				ncount += 1
			
			total += abs(val)
			
			if gmin is None:
				gmin = abs(val)
			else:
				gmin = min(gmin, abs(val))
				
	if zero:
		return total
		
	if ncount % 2 == 0:
		return total
	
	else:
		return total - (2*gmin)
				


# Main
t = read_int()
for case in range(t):
	n, m = read_ints()
	a = []
	for _ in range(n):
		a.append(read_ints())
		
	sol = solve(n, m, a)
	print (sol)
