#!/usr/bin/python3

# Codeforces - Testing Round 16
# Problem B - Square? 


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(a1, b1, a2, b2):
	if a1 == a2:
		if b1 + b2 == a1:
			return 'Yes'
	
	if a1 == b2:
		if b1 + a2 == a1:
			return 'Yes'
			
	if b1 == a2:
		if a1 + b2 == b1:
			return 'Yes'
		
	if b1 == b2:
		if a1 + a2 == b1:
			return 'Yes'
	
	return 'No'

# Main
t = read_int()
for case in range(t):
	a1, b1 = read_ints()
	a2, b2 = read_ints()
	
	sol = solve(a1, b1, a2, b2)
	print (sol)
