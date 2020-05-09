#!/usr/bin/python3

# Codeforces - Round 640
# Problem A - Sum of Round Numbers


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n):
	s = str(n)
	l = len(s)
	sol = []
	for i in range(l):
		val = s[i]
		if val != '0':
			si = val + '0' * (l - i - 1)
			sol.append(si)
	
	return sol


# Main
t = read_int()
for case in range(t):
	n = read_int()
	sol = solve(n)
	
	print (len(sol))
	print (" ".join(sol))
