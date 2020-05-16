#!/usr/bin/python3

# Codeforces - Round #643
# Problem A - Sequence with Digits


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---
def f(n):
	l = [x for x in str(n)]
	mn = int(min(l))
	mx = int(max(l))
	return n + mn * mx


def solve(a, k):
	ai = a
	for i in range(k-1):
		ai = f(a)
		if ai == a:
			return ai
		else:
			a = ai
			
	return ai

# Main
t = read_int()
for case in range(t):
	a1, k = read_ints()
	sol = solve(a1, k)
	
	print (sol)
