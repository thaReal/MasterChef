#!/usr/bin/python3

# Codeforces - Round 633
# Problem B - Sorted Adjacent Differences 


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	
	
def solve(n, a):
	a.sort()
	sol = []
	idx = (n // 2)
	if n % 2 == 0:
		idx -=1
	inc = 0
	side = -1
	
	for i in range(n):
		idx += inc * side
		sol.append(str(a[idx]))
		
		inc += 1
		side = -1 if side == 1 else 1
		
	return (sol)
		

# Main
t = read_int()
for case in range(t):
	n = read_int()
	a = read_ints()
	
	sol = solve(n, a)
	print (" ".join(sol))
