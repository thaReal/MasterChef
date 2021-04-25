#!/usr/bin/python3      

'''
Codejam 2021 - Round 1B
Problem: "Digit Blocks"
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
def solve(n):
    pass
	

# Main
T = read_int()
for i in range(T):
    n = read_int()
    sol = solve(n)
	
	# Output
    print ("Case #{}: {}".format(i+1, sol))
