#!/usr/bin/python3

# Codeforces - Round #675
# Author: frostD
# Problem C - Bargain


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n):
	l = len(n)
	dp = [0 for x in range(l)]
	
	dp[0] = int(n[0])
	res = dp[0]

	for i in range(1, l):
		ni = int(n[i])
		dp[i] = (i+1) * ni + 10 * dp[i-1]
		res += dp[i]
		
	return res

# Main
n = input()
sol = solve(n)
print (sol)
