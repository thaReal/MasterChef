#!/usr/bin/python3
'''
Codejam 2020 - Round 1A 
Problem: "Pattern Matching"
Author: Daniel Ruland
'''

# Only valid for parts 1 and 2


MAX_LETTERS = 10000

# Utilility Functions
def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

def solve(p):
	lens1 = [len(pi[0]) for pi in p]
	lens2 = [len(pi[1]) for pi in p]
	
	mx_len1 = lens1.index(max(lens1))
	mx_len2 = lens2.index(max(lens2))

	mx1 = p[mx_len1][0]
	mx2 = p[mx_len2][1]

	# first list
	for pi in p:
		if mx1 == pi[0]:
			continue
			
		idx = len(pi[0])
		if mx1[:idx] == pi[0]:
			continue
		else:
			return '*'
	
	# second list
	for pi in p:
		if mx2 == pi[1]:
			continue
			
		idx = len(mx2) - len(pi[1])
		if mx2[idx:] == pi[1]:
			continue
		else:
			return '*'
	
	return mx1 + mx2
		
	
	
# Main
T = read_int()
for i in range(T):
	N = read_int()
	p = []
	for j in range(N):
		p.append(input().split('*')) 
		
	sol = solve(p)
	
	# Output - Test Case 1 & 2 Solution
	print ("Case #{}: {}".format(i+1, sol))
