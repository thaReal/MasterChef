#!/usr/bin/python3

'''
Codejam 2019 Qualification Round [Practice] 
Problem: "Forgone Solution"
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
def solve(N):
	A = ''
	B = ''
	
	for char in str(N):
		if char != '4':
			A += char
			B += '0'
		else:
			A += '3'
			B += '1'
	
	B = B.lstrip('0')
	
	return A, B

# Main
T = read_int()
for i in range(T):
	# Solution
	N = read_int()
	A, B = solve(N)
	
	# Output
	print ("Case #{}: {} {}".format(i+1, A, B))
