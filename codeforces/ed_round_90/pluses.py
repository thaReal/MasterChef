#!/usr/bin/python3

# Codeforces - Educational Round 90
# Author: frostD
# Problem C - Pluses and Minuses


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---
	
def solve(s):
	l = len(s)
	cur = 0
	res = 0
	dp = [0 for _ in range(l+1)]
	
	for i in range(l):
		if s[i] == '+':
			dp[i+1] = dp[i] + 1
			cur += 1
			
		else:
			if cur > 0:
				dp[i+1] = dp[i] + 1
				cur -= 1

			else:
				dp[i+1] = dp[i] + (i+2)

	return dp[-1]
	
	

# Main
t = read_int()
for case in range(t):
	s = input()
	sol = solve(s)
	print (sol)
	
	
'''
def solve(s):
	# Psuedocode Version
	res = 0
	init = 0
	while True:
		cur = init
		ok = True
		for i in range(1, len(s)+1):
			res += 1
			if s[i-1] == '+':
				cur += 1
			else:
				cur -= 1
			
			if cur < 0:
				ok = False
				break
		
		if ok:
			break
		
		init +=1

	return res
'''
