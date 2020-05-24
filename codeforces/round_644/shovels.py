#!/usr/bin/python3

# Codeforces - Round 644
# Problem D - Buying Shovels

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	


def largestFactor(n): 
	if n <= 3:
		return 1
	if n % 2 == 0:
		return n // 2
	elif n % 3 == 0: 
		return n // 3
	i = 5
	while(i * i <= n): 
		if n % i == 0: 
			return n // i
		elif n % (i + 2) == 0: 
			return n // (i + 2)
		i = i + 6
	return 1



def solve(n, k):
	if k >= n:
		return 1
	
	if n % k == 0:
		return n // k
	
	lf = largestFactor(n)
	return lf


# Main
t = read_int()
for case in range(t):
	n, k = read_ints()
	sol = solve(n, k)
	
	print (sol)
