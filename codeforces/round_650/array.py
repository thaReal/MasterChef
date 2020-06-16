#!/usr/bin/python3

# Codeforces - Round 650
# Author: frostD
# Problem B - Even Array


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, a):
	wrong_odds = 0
	wrong_evens = 0
	for i in range(n):
		if i % 2 == 0:
			if a[i] % 2 != 0:
				wrong_evens += 1
		else:
			if a[i] % 2 == 0:
				wrong_odds += 1
		
	if wrong_odds != wrong_evens:
		return -1
		
	return wrong_odds


# Main
t = read_int()
for case in range(t):
	n = read_int()
	a = read_ints()
	sol = solve(n, a)
	print (sol)
