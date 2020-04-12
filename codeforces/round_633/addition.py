#!/usr/bin/python3

# Codeforces - Round 633
# Problem C - Powered Addition


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	
	
def solve(n,a):
	if n == 1:
		return 0
		
	l_delta = []
	for i in range(n-1):
		if a[i] <= a[i+1]:
			l_delta.append(0)
		else:
			l_delta.append(a[i] - a[i+1])
			a[i+1] = a[i]
	
	mx = max(l_delta)
	
	if mx == 0:
		sol = 0
	else:
		sol = len(bin(mx)[2:])
	
	return sol
	

# Main
t = read_int()
for case in range(t):
	n = read_int()
	a = read_ints()
	
	sol = solve(n, a)
	print (sol)
