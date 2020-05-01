#!/usr/bin/python3

# Codeforces Round 638
# Author: Daniel Ruland
# Problem B Phoenix and Beauty

from collections import deque

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---
def solve(n,k,a):
	if k == 1:
		if len(set(a)) != 1:
			return -1
		else:
			return [len(a), [str(x) for x in a]]
	
	sol = []
	subset = deque(a[:k])
	target = sum(subset)
	
	da = deque(a[k:])
	while len(da) > 0:
		v0 = subset.popleft()
		sol.append(v0)
		
		val = da.popleft()
		if sum(subset) + val == target:
			subset.append(val)
		
		else:
			for i in range(k-1):
				v1 = target - sum(subset)
				if v1 < 1:
					return -1
				
				subset.append(v1)
				v0 = subset.popleft()
				sol.append(v0)
				
				#FUCK!!!

			if sum(subset) != target:
				if len(da) != 0:
					return -1
					
				else:
					v0 = subset.popleft()
					sol.append(v0)
					v1 = target - sum(subset)
					if v1 > 0:
						subset.append(v1)
					else:
						return -1
						
	sol = sol + list(subset)					
		
	return [len(sol), [str(x) for x in sol]]
	
	


# Main
t = read_int()
for case in range(t):
	n, k = read_ints()
	a = read_ints()
	sol = solve(n, k, a)
	
	if sol == -1:
		print (sol)
		
	else:
		print (sol[0])
		print (' '.join(sol[1]))
