#!/usr/bin/python3      

'''
Codejam 2021 - Round 1B
Problem: "Digit Blocks"
Author: Daniel Ruland
'''
import sys
from collections import deque

# Utility Functions
def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	
	
def interact(output):
	print(output)
	sys.stdout.flush()


# Solution:
def solve(n, b, p):
	town = [[] for x in range(n)]
	finish = deque()
	min_size = deque()
	
	for i in range(b-1):
		d = read_int()
		town[0].append(d)
	
	finish.append(0)
	
	
	
	for i in range((b-1)*(n//4)):
		d = read_int()
		bldg = i // (b-1)
		town[bldg].append(d)
		interact(bldg+1)
	
	min_bldg = n-1
	for i in range((n*b) - (b-1)*(n//4)):
		d = read_int()
		
		if d <= 7:
			for j in range(n-1, 0, -1):
				if len(town[j]) < b:
					town[j].append(d)
					interact(j+1)
			
		else:
			for j in range(n):
				if len(town[j]) < b:
					town[j].append(d)
					interact(j+1)
	

# Main
T, n, b, p = read_ints()
for i in range(T):
    sol = solve(n, b, p)
    
result = read_int()
sys.exit(0)
