#!/usr/bin/python3

# Codeforces - Round 655
# Author: frostD
# Problem C - Omkar and Baseball


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, a):
	valid = [0 for _ in range(n)]
	for i in range(n):
		if a[i] != i+1:
			valid[i] = 1
			
	if 1 not in valid:
		return 0
		
	if 0 not in valid:
		return 1

	cnt = 0
	for i in range(n-1):
		if valid[i] != valid[i+1]:
			cnt += 1
			
		if cnt > 2:
			return 2
	
	if cnt == 2 and valid[0] == 1:
		return 2			
	
	return 1


# Main
t = read_int()
for case in range(t):
	n = read_int()
	a = read_ints()
	sol = solve(n, a)
	print (sol)
