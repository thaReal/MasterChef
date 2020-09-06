#!/usr/bin/python3

# Codeforces - Round 668
# Author: frostD
# Problem B - Array Cancellation


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints


#---

def solve(n, a):
	# Need to do this in one pass 
	
	rtotal = 0
	non_free = 0
	for ai in a:
		if rtotal > 0 and ai < 0:
			if rtotal >= abs(ai):
				rtotal += ai
			else:
				non_free = abs(ai + rtotal)
				rtotal += ai
			
			continue
		
		if rtotal >= 0 and ai > 0:
			rtotal += ai
			continue
			
		if rtotal < 0 and ai > 0:
			if abs(rtotal) >= ai:
				rtotal += ai
			else:
				non_free = abs(ai + rtotal)
				rtotal += ai

			continue
			
		if rtotal <= 0 and ai < 0:
			rtotal += ai
			non_free -= ai
			continue
			
	print ("rtotal: {}, non_free: {}".format(rtotal, non_free))
	 	
	return non_free
	
	
def solve2(n, a):
	# Need to solve this in one pass
	# Also we know the sum of the array has to be = 0 per the problem description
	
	dp = [[0 for x in range(n)] for y in range(2)]
	for i in range(n):
		if i == 0:
			if a[i] > 0:
				dp[0][0] = a[i]
			
			dp[1][0] = abs(a[i])
		
		if a[i] >= 0:
			dp[0][i] = dp[0][i-1] + a[i]
			dp[1][i] = dp[1][i-1] + a[i]
		else:
			dp[0][i] = dp[0][i-1]
			
			
		if a[i] < 0:
			if dp[0][i] > 0:
				if dp[0][i] >= abs(a[i]):
					dp[0][i] += a[i]
					dp[1][i] = dp[1][i-1] + a[i]
				else:
					dp[1][i] = dp[1][i-1] - abs(a[i] + dp[0][i])
					dp[0][i] = 0
			
			else:
				dp[1][i] = dp[1][i-1] + abs(a[i])
				
			
	return dp[0][-1]
			
	

# Main
t = read_int()
for case in range(t):
	n = read_int()
	a = read_ints()
	
	sol = solve2(n, a)
	print (sol)
