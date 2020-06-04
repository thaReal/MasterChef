#!/usr/bin/python3

# Codeforces - Round 647
# Author: frostD
# Problem A - Johnny and Ancient Computer


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(a, b):
	if a == b:
		return 0
		
	a, b = min(a,b), max(a,b)
	

		
	ba = bin(a)
	bb = bin(b)
	if bb.find(ba) != 0:
		return -1
	
	l = len(ba)
	shift = bb[l:]
	if shift.count('1') != 0:
		return -1
	cntr = len(shift)
	
	res = 0
	res += cntr // 3
	cntr = cntr % 3
	
	res += cntr // 2
	cntr = cntr % 2
	
	res += cntr
	
	return res
	
	

# Main
t = read_int()
for case in range(t):
	a, b = read_ints()
	sol = solve(a, b)
	print (sol)
