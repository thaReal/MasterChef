#!/usr/bin/python3      

'''
Codejam 2021 - Round 1A
Problem: "Append Sort"
Author: Daniel Ruland
'''

# Utility Functions
def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	
	
# Solution:
def solve(n, x):
	ret = 0
    
	for i in range(1, n):
		while x[i] <= x[i-1]:
			x[i] *= 10
			
			if x[i-1] - x[i] < 9 and x[i-1] - x[i] >= 0:
				x[i] += (x[i-1] - x[i]) + 1
			
			ret += 1
	
	return ret

# Main
T = read_int()
for i in range(T):
    n = read_int()
    x = read_ints()
    sol = solve(n, x)
	
	# Output
    print ("Case #{}: {}".format(i+1, sol))
