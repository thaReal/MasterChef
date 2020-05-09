#!/usr/bin/python3

# Codeforces - Round 640
# Problem C - K-th Not Divisible by n


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n,k):
	cntr = k // (n-1)
	sol = cntr + k
	
	if sol % n == 0:
		sol -= 1
	
	return sol

# Main
t = read_int()
for case in range(t):
	n, k = read_ints()
	sol = solve(n,k)
	
	print (sol)
