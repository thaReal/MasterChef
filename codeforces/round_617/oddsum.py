#!/usr/bin/python3

# Codeforces - Round 617 - Practice
# Author: frostD
# Problem A - Array with Odd Sum


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n,a):
	odd = False
	even = False
	if sum(a) % 2 == 1:
		return "YES"
	
	for i in range(n):
		if a[i] % 2 == 1:
			odd = True
		else:
			even = True
		
		if odd and even:
			return "YES"
	
	return "NO"	


# Main
t = read_int()
for case in range(t):
	n = read_int()
	a = read_ints()
	sol = solve(n,a)
	print (sol)
