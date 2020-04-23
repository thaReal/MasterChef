#!/usr/bin/python3

# Codeforces - Round 637
# Problem B - Nastya and Door 

from collections import deque

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n,k,a):
	if a[0] > a[1]:
		peak_map = [1]
	else:
		peak_map = [0]
		
	i = 1
	while i <= n-2:
		seg = a[i:i+3]
		if max(seg) == seg[1]:
			peak_map += [0, 1, 0]
			i += 3
		else:
			peak_map += [0]
			i += 1
			
	if a[n-1] > a[-2]:
		if len(peak_map) != n:
			peak_map += [1]
		else:
			peak_map[-1] = 1
	else:
		if len(peak_map) != n:
			peak_map += [0]
		else:
			peak_map[-1] = 0
		
	return peak_map
		


# Main
t = read_int()
for case in range(t):
	n, k = read_ints()
	a = read_ints()
	
	peak_map = solve(n,k,a)
	
	print ("{}".format(peak_map))
