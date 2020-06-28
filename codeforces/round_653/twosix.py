#!/usr/bin/python3

# Codeforces - Round #653 (Div. 3)
# Author: frostD
# Problem B - Multiply by 2, Divide by 6


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n):
	if n == 1:
		return 0
	
	moves = 0
	while n != 1:
		if n % 6 == 0:
			n //= 6
			moves += 1
		
		elif (n * 2) % 6 == 0:
			n *= 2
			moves += 1
		
		else:
			break
	
	if n != 1:
		return -1
	else:
		return moves
		
	


# Main
t = read_int()
for case in range(t):
	n = read_int()
	sol = solve(n)
	print (sol)
