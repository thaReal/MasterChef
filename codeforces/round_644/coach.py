#!/usr/bin/python3

# Codeforces - Round 644
# Problem B - Honest Coach


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, s):
	s.sort()
	min_diff = max(s)
	for i in range(1, len(s)):
		diff = s[i] - s[i-1]
		min_diff = min(min_diff, diff)
		
	return min_diff


# Main
t = read_int()
for case in range(t):
	n = read_int()
	s = read_ints()
	sol = solve(n, s)
	
	print (sol)
