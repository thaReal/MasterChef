#!/usr/bin/python3

# Codeforces - Round 641
# Author - FrostD
# Problem A - Orac and Factors


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def smallest_divisor(n):
	for i in range(2, n//2 + 1):
		if n % i == 0:
			return i
	return n
	

def solve(n, k):
	fn = n
	for i in range(k):
		if fn % 2 == 0:
			mult = k - i
			fn += 2 * mult
			return fn
			
		else:
			sd = smallest_divisor(fn)
			fn += sd 
	
	return fn


# Main
t = read_int()
for case in range(t):
	n, k = read_ints()
	sol = solve(n, k)
	
	print (sol)
