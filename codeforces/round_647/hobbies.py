#!/usr/bin/python3

# Codeforces - Round 647
# Author: frostD
# Problem B - Johnny and His Hobbies


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, S):
	res = 0
	s = set(S)
	for i in range(1, 1024):
		sn = set()
		for si in s:
			sni = si ^ i
			if sni in s:
				sn.add(sni)
			else:
				break
		if sn == s:
			return i
				
	return -1
	
	
# Main
t = read_int()
for case in range(t):
	n = read_int()
	S = read_ints()
	sol = solve(n, S)
	
	print (sol)
