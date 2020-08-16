#!/usr/bin/python3

# Codeforces - Global Round 10
# Author: frostD
# Problem A - Omkar and Password


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, a):
	'''
	while len(set(a)) != 1:
		l = len(a)
		for i in range(l-1):
			if i >= len(a) - 1:
				break
				
			if a[i] != a[i+1]:
				a[i] = a[i+1] + a[i]
				a = a[:i+1] + a[i+2:]
				
		if len(a) == l:
			break
	
	print (a)
	return len(a)
	'''
	
	if len(set(a)) == 1:
		return len(a)
	
	return 1
			
			

# Main
t = read_int()
for case in range(t):
	n = read_int()
	a = read_ints()
	sol = solve(n, a)
	print (sol)
