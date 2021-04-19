#!/usr/bin/python3

'''
Kickstart 2021 - Round B 
Problem: "Increasing Substring"
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
def solve(n, s):
	dp = [1 for x in range(n)]
	
	for i in range(1, n):
		if s[i] > s[i-1]:
			dp[i] = dp[i-1] + 1
		
		
	return ' '.join([str(x) for x in dp])
	

# Main
t = read_int()
for i in range(t):
	# Solution
	n = read_int()
	s = input()
	sol = solve(n, s)
	
	# Output
	print ("Case #{}: {}".format(i+1, sol))
