#!/usr/bin/python3

# Codeforces - Round #673
# Author: frostD
# Problem B - Two Arrays 

from collections import Counter

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, T, a):
	sol = [0] * n

	c = Counter()
	d = Counter()
	
	c[T - a[0]] += 1
	sol[0] = 1
	
	for i in range(1, n):
		c_cnt = 0
		d_cnt = 0
		if a[i] in c.keys():
			c_cnt += c[a[i]]
			
		if a[i] in d.keys():
			d_cnt += d[a[i]]

		if min(c_cnt, d_cnt) == c_cnt:
			c[T - a[i]] += 1
			sol[i] = 1
		
		else:
			d[T - a[i]] += 1

	return ' '.join([str(x) for x in sol])
	


# Main
t = read_int()
for case in range(t):
	n, T = read_ints()
	a = read_ints()
	sol = solve(n, T, a)
	print (sol)
