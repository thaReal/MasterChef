#!/usr/bin/python3

# Codeforces - Educational Round #90
# Author: frostD
# Problem D - Maximum Sum on Even Positions


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, a):
	diff = [0 for _ in range(n-1)]
	for i in range(n-1):
		if i % 2 == 0:
			diff[i] = a[i] - a[i+1]
		else:
			diff[i] = a[i+1] - a[i]
		
	evens_diff = diff[::2]
	odds_diff = diff[1:2]
	
	# non offset
	dp_e = [0 for _ in range(len(evens_diff) + 1)]
	for i in range(len(evens_diff)):
		if dp_e[i] + evens_diff[i] < 0:
			dp_e[i+1] = dp_e[i] + evens_diff[i]
		else:
			dp_e[i+1] = 0
	
	# 1 pos offset
	dp_o = [0 for _ in range(len(odds_diff) + 1)]
	for i in range(len(odds_diff)):
		if dp_o[i] + odds_diff[i] < 0:
			dp_o[i+1] = dp_o[i] + odds_diff[i]
		else:
			dp_o[i+1] = 0
	
	delta = min(min(dp_e), min(dp_o))
	sol = sum(a[::2]) - delta
	
	# Debug
	#print (dp_e)
	#print (dp_o)
	#print (evens_diff)
	#print (odds_diff)
	
	return sol
	


# Main
t = read_int()
for case in range(t):
	n = read_int()
	a = read_ints()
	sol = solve(n, a)
	print (sol)
