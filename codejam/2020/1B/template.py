#!/usr/bin/python3
'''
Codejam 2020 - Round 1B
Problem: ""
Author: Daniel Ruland
'''

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	
	
def solve():
	pass



# Main
T = read_int()
for x in range(T):
	# Solution
	sol = solve()
	
	# Output
	print ("Case #{}: {}".format(x+1, sol))
