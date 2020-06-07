#!/usr/bin/python3

# Codeforces - Round 648
# Author: frostD
# Problem B - Trouble Sort


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, a, b):
	elems = list(zip(a, b))
	i = 0
	while i < n-1:
		if elems[i][0] <= elems[i+1][0]:
			i += 1
			
		elif elems[i][1] != elems[i+1][1]:
			elems[i], elems[i+1] = elems[i+1], elems[i]

			# my guess is that this is causing an error 
			# on a boundary case			
			if i != 0:
				i -= 1
			
		else:
			return 'No'
			
			
	return 'Yes' 
	
	


# Main
t = read_int()
for case in range(t):
	n = read_int()
	a = read_ints()
	b = read_ints()
	
	sol = solve(n, a, b)
	print (sol)
