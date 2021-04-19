#!/usr/bin/python3

'''
Kickstart 2021 - Round B 
Problem: "Longest Progression"
Author: Daniel Ruland
'''

from collections import deque

# Utility Functions
def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	
	
# Solution:
def solve(n, a):
	if len(a) == 1:
		return "0"
	
	if len(a) == 2:
		return "1"
	
	arry = []
	for i in range(1, n):
		arry.append(a[i] - a[i-1])
	
	mx = 1
	local_mx = 1
	# iterate through each postion and see if we can change any
	for i in range(n-2):
		if arry[i] == arry[i+1]:
			local_mx += 1
			continue
			
		if i == n-3:
			mx = max(mx, local_mx + 1)
			continue
			
		if (arry[i+1] + arry[i+2]) % 2 == 0 and (arry[i+1] + arry[i+2]) // 2 == arry[i]:
			cand = arry.copy()
			cand[i+1] = cand[i]
			cand[i+2] = cand[i]
			
			j = i
			while j < n-2:
				if cand[j] == cand[j+1]:
					local_mx += 1
					j += 1
				else:
					break
					
			mx = max(mx, local_mx)
		
		local_mx = 1	

	mx = max(mx, local_mx)	
	
			
	return mx + 1
	
# Main
t = read_int()
for i in range(t):
	# Solution
	n = read_int()
	a = read_ints()
	sol = solve(n, a)
	
	# Output
	print ("Case #{}: {}".format(i+1, sol))
