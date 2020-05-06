#!/usr/bin/python3

# Codeforces - Round 639
# Problem D - Monopole Magnets 

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, m, grid):
	pcs = 0
	for i in range(n):
		prev_color = None
		for j in range(m):
			color = grid[n][m]
				 


# Main
n, m = read_ints()
grid = []
for i in range(n):
	line = input()
	gline = []
	for j in line:
		val = 1 if j == '.' else 0
		gline.append(val)
	grid.append(gline)

sol = solve(n, m, grid)
