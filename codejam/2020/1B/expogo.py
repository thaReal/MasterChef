#!/usr/bin/python3
'''
Codejam 2020 - Round 1B
Problem: "Expogo"
Author: Daniel Ruland
'''

# Slow solution; need to check the absolute distance mathmatically before
# attempting to step in order to complete the larger test sets

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
		

def jump(n):
	steps = []
	i = 1
	while sum(steps) < n:
		steps.append(pow(2, i-1))
		i += 1
	
	return steps
		
	
def solve(x, y):
	x0 = 0
	y0 = 0
	
	if x%2 == 1 and y%2 == 1:
		return "IMPOSSIBLE"
		
	if x%2 == 0 and y%2 == 0:
		return "IMPOSSIBLE"
		
	dist = abs(x) + abs(y)
	step_sz = jump(dist)
	steps = []
	for s in step_sz[::-1]:
		if abs(y) >= abs(x):
			if y > 0:
				y -= s
				steps.append('N')
			else:
				y += s
				steps.append('S')
		else:
			if x > 0:
				x -= s
				steps.append('E')
			else:
				x += s
				steps.append('W')
	

	if x != 0 or y != 0:
		return "IMPOSSIBLE"
	
	return ''.join(steps[::-1])
	

# Main
T = read_int()
for i in range(T):
	x, y = read_ints()
	sol = solve(x, y)
	
	# Output
	print ("Case #{}: {}".format(i+1, sol))
