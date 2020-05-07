#!/usr/bin/python3

# Codeforces - Testing Round 16
# Problem C - Skier


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(chars):
	x0 = 0
	y0 = 0
	paths = set()
	
	time = 0
	for c in chars:
		if c == 'N':
			y = y0 + 1
			x = x0
			
		if c == 'S':
			y = y0 - 1
			x = x0
			
		if c == 'E':
			x = x0 + 1
			y = y0
			
		if c == 'W':
			x = x0 - 1
			y = y0
			
		path = (x0, y0, x, y)
		path_mir = (x, y, x0, y0)
		
		if path in paths or path_mir in paths:
			time += 1
		else:
			time += 5
			
		paths.add(path)
		x0 = x
		y0 = y
	
	return time


# Main
t = read_int()
for case in range(t):
	chars = input()
	sol = solve(chars)
	
	print (sol)
