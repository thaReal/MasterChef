#!/usr/bin/python3

# Codeforces - Round 651
# Author: frostD
# Problem B - GCD Compression


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, a):
	l = n - 1
	mod2 = [x % 2 for x in a]
	selected = [0 for _ in range(2*n)]
	pairs = []
	
	for i in range(2*n):
		if selected[i] == 1:
			continue
			
		ai = a[i]
		parity = mod2[i]
		for j in range(len(a[i+1:])):
			if selected[i+j+1] == 0:
				if mod2[i+j+1] == parity:
					# Match Found
					pairs.append([i, i+j+1])
					selected[i] = 1
					selected[i+j+1] = 1
					break
		
		if len(pairs) == l:
			break
					
	
	return pairs

# Main
t = read_int()
for case in range(t):
	n = read_int()
	a = read_ints()
	
	sol = solve(n, a)
	for pair in sol:
		print ("{} {}".format(pair[0]+1, pair[1]+1))
