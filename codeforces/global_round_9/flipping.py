#!/usr/bin/python3

# Codeforces - Global Round 9 
# Author: frostD
# Problem A - Sign Flipping


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, a):
	neg = 0
	pos = 0
	zero_diff = []
	diffs = []
	
	for i in range(1, n):
		di = a[i] - a[i-1]
		if di < 0:
			neg += 1
		
		elif di > 0:
			pos += 1
	
		else:
			pos += 1
			neg += 1
			
	if pos < ((n-1) // 2) or neg < ((n-1) // 2):  
		# Start here I guess..
		
		
		for i in range(n-1):
			if neg < ((n-1) // 2):
				if a[i+1] - a[i] > 0:
					if (a[i+1] * -1) - a[i] < 0:
						a[i+1] = a[i+1] * -1
						neg += 1
						if a[i+1] - a[i] < 0:
							pos -= 1
							
			if pos < ((n-1) // 2):
				if a[i+1] - a[i] < 0:
					if (a[i+1] * -1) - a[i] > 0:
						a[i+1] = a[i+1] * -1
						pos += 1
						if a[i+1] - a[i] > 0:
							neg -= 1

			if pos >= ((n-1) // 2) and neg >= ((n-1) // 2):
				break
	
	return " ".join([str(x) for x in a])
	
	
# Main
t = read_int()
for case in range(t):
	n = read_int()
	a = read_ints()
	sol = solve(n, a)
	print (sol)
