#!/usr/bin/python3

# Codeforces - Round 663
# Author: frostD
# Problem A - Suborrays


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n):
	nums = [str(x) for x in range(1,n+1)]
	idx = n // 2
	sol = []
	sol.append(nums[idx])
	
	i = 1
	while len(sol) < n:
		sol.append(nums[idx - i])
		if len(sol) < n:
			sol.append(nums[idx + i])
		i += 1
	
	return sol


# Main
t = read_int()
for case in range(t):
	n = read_int()
	sol = solve(n)
	
	print (' '.join(sol))
