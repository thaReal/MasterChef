#!/usr/bin/python3

# Codeforces - Educational Round 84
# Problem A - Sum of Odd Integers


# Utilility Functions

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

def solve(n, k):
	# if n is even
	if k > n:
		return "NO"
		
	if n % 2 == 0:
		if k % 2 != 0:
			return "NO"
			
	# if n is odd
	else:
		if k % 2 != 1:
			return "NO"
	
	if pow(k, 2) > n:
		return "NO"
	
	return "YES"
		

# Main
t = read_int()
for i in range(t):
	data = read_ints()
	n = data[0]
	k = data[1]
	print (solve(n, k))

		
