#!/usr/bin/python3

# Codeforces - Global Round 10
# Author: frostD
# Problem C - Omkar and Waterslide


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, a):
	b = a[::-1]
	opr = 0
	for i in range(n-1):
		if b[i] < b[i+1]:
			opr += b[i+1] - b[i]
	
	return opr
	


# Main
t = read_int()
for case in range(t):
	n = read_int()
	a = read_ints()
	
	sol = solve(n, a)
	print (sol)
