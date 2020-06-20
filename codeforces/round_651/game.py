#!/usr/bin/python3

# Codeforces - Round 651
# Author: frostD
# Problem C - Number Game

import math

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n):
	turn = 0
	
	# Boundary Cases (probably not neccesary - part of my mad dash at the end)
	if n == 1:
		return "FastestFinger"
	
	if n % 2 == 1:
		return "Ashishgup"
		
	while n > 1:
		turn += 1
			
		divisor = None
		for i in range(3, n+1, 2):
		    if n % i == 0:
		        divisor = i
		
		if divisor == None:
			n -= 1
		else:
			n //= divisor
		
		
	if turn % 2 == 0:
		return "FastestFinger"
		
	else:
		return "Ashishgup"
	


# Main
t = read_int()
for case in range(t):
	n = read_int()
	sol = solve(n)
	print (sol)
