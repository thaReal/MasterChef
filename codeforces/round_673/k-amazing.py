#!/usr/bin/python3

# Codeforces - Round #673
# Author: frostD
# Problem C - k-Amazing Numbers 


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---
def get_amazing_number(n, a, k):
	s = set(a[:k])
	for i in range(1, n-k+1):
		s.intersection_update(a[i:i+k])
		
		if len(s) == 0:
			return -1

	return min(s)


def solve(n, a):
	sol = [-1] * n
	mn = min(a)
	sol[-1] = mn
	
	left = 1
	right = n-1
		
	while left < right:
		sol[left] = get_amazing_number(n,a,left+1)
		sol[right] = get_amazing_number(n,a,right+1)
		
		if sol[left] != sol[right]:
			left += 1
			right -= 1
		
		else:
			for i in range(left+1, right):
				sol[i] = sol[left]
			break
					

	return ' '.join([str(x) for x in sol])

# Main
t = read_int()
for case in range(t):
	n = read_int()
	a = read_ints()
	sol = solve(n, a)
	print (sol)
