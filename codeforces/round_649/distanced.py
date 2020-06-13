#!/usr/bin/python3

# Codeforces - Round 649
# Author: frostD
# Problem B - Most Socially Distanced Subsequence


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, p):
	res = n
	inc = True if p[1] > p[0] else False
	idx = [0 for _ in range(n)]
	idx[0] = 1
	idx[-1] = 1
	
	for i in range(1, n-1):
		if inc:
			if p[i+1] > p[i]:
				res -= 1
			else:
				inc = False
				idx[i] = 1
		else:
			if p[i+1] < p[i]:
				res -= 1
			else:
				inc = True
				idx[i] = 1
	
	arr = []
	for i in range(n):
		if idx[i] == 1:
			arr.append(str(p[i]))
			
	return res, arr
	
	

# Main
t = read_int()
for case in range(t):
	n = read_int()
	p = read_ints()
	
	res, arr = solve(n, p)
	print (res)
	print (' '.join(arr))
