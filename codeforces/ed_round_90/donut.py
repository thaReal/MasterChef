#!/usr/bin/python3

# Codeforces - Educational Round 90 
# Author: frostD
# Problem A - Donut Shop


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(a, b, c):
	if c <= a:
		shop1 = -1
	else:
		shop1 = 1
		
	shop2 = b if a*b > c else -1
	
	return (str(shop1), str(shop2))
		


# Main
t = read_int()
for case in range(t):
	a, b, c = read_ints()
	sol = solve(a, b, c)
	print (' '.join(sol))
