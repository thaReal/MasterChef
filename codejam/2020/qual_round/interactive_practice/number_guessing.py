#!/usr/bin/python3
'''
Codejam 2020 - Practice
Problem: "Number Guessing"
Author: Daniel Ruland
'''

import sys

# Utilility Functions
def read_int():
	n = int(input())
	return n

def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	
def solve(lb, ub, n):
	guess = int((lb + ub) / 2)
	print (guess)
	sys.stdout.flush()
	
	response = input()
	
	if response == 'CORRECT':
		return
	
	elif response == 'TOO_BIG':
		solve(lb, guess-1, n-1)
	
	elif response == 'TOO_SMALL':
		solve(guess+1, ub, n-1)
	
	else:
		sys.exit(0)
		
# Main
t = read_int()
for x in range(t):
	lb, ub = read_ints()
	n = read_int()
	solve(lb, ub, n)
