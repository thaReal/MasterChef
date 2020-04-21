#!/usr/bin/python3

# Codeforces - Round 636
# Problem A - Candies


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n):
	k = 2
	ksum = 3
	while n % ksum != 0:		
		k += 1
		ksum += pow(2, k-1)
	
	return n // ksum

# Main
t = read_int()
for case in range(t):
	n = read_int()
	
	sol = solve(n)
	print (sol)
