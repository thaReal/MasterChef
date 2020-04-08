#!/usr/bin/python3

# Codeforces - Round 632
# Problem B - Kind Anton 


# Utilility Functions

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

def solve(n, a, b):
	if a[0] != b[0]:
		return 'NO'
		
	for i in range(1, n):
		if a[i] != b[i]:
			nums = set(a[:i])
			if a[i] > b[i]:
				if -1 not in nums:
					return 'NO'
					
			if a[i] < b[i]:
				if 1 not in nums:
					return 'NO'
	
	return 'YES'
			
		
		
		
	
	
# Main
t = read_int()
for case in range(t):
	n = read_int()
	a = read_ints()
	b = read_ints()
	
	sol = solve(n, a, b)
	print (sol)
