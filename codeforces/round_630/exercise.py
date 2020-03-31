#!/usr/bin/python3

# Codeforces - Round 630
# Problem A - Exercising Walk


# Utilility Functions

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

def solve():
	a, b, c, d = read_ints()
	x, y, x1, y1, x2, y2 = read_ints()
	
	# set starting point at 0
	x1 = x1 - x
	x2 = x2 - x
	y1 = y1 - y
	y2 = y2 - y
	
	dx = b - a
	dy = d - c
	
	
	
	if a < b:
		if x2 < dx:
			return "No"
	elif a > b:
		if x1 > dx:
			return "No"
	else:
		if x1 == 0 and x2 == 0:
			if a != 0 or b != 0:
				return "No"
	
	if c < d:
		if y2 < dy:
			return "No"
	elif c > d:
		if y1 > dy:
			return "No"
	else:
		if y1 == 0 and y2 == 0:
			if c != 0 and d != 0:
				return "No"
	
	return "Yes"
	
					

# Main
t = read_int()
for i in range(t):
	print(solve())
			
