#!/usr/bin/python3

# Codeforces - Round 639
# Problem A - Puzzle Pieces

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n,m):
	if n + m > 4:
		if n == 1 or m == 1:
			return 'YES'
	
		return 'NO'
	
	else:
		return 'YES'


# Main
t = read_int()
for case in range(t):
	n, m = read_ints()
	sol = solve(n,m)
	
	print (sol)
