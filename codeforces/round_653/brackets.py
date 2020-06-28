#!/usr/bin/python3

# Codeforces - Round #653 (Div. 3)
# Author: frostD
# Problem C - Move Brackets


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, s):
	dp = [[0 for _ in range(n)] for _ in range(2)]
	for i in range(n):
		dp[0][i] = 1 if s[i] == '(' else -1
		dp[1][i] = dp[1][i-1] + dp[0][i] if i != 0 else dp[0][i]
		
	sol = min(dp[1]) * -1
	if sol < 0:
		return 0
	
	return sol


# Main
t = read_int()
for case in range(t):
	n = read_int()
	s = input()
	sol = solve(n, s)
	print (sol)
