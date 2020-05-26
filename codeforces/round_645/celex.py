#!/usr/bin/python3

# Codeforces - Round 645
# Author: frostD
# Problem C - Celex Update


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	
	if dx == 0 or dy == 0:
		return 1
	
	res = min(dx, dy) * max(dx, dy) + min(dx, dy)
	return res


# Main
t = read_int()
for case in range(t):
	x1, y1, x2, y2 = read_ints()
	sol = solve(x1, y1, x2, y2)
	
	print (sol)
