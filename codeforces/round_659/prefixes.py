#!/usr/bin/python3

# Codeforces - Round #659 [Virtual Practice]
# Author: frostD
# Problem A - Common Prefixes


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(a, n):
	letters = "abcdefghijklmnopqrstuvwxyz"
	ret = []
	l = max(a)
	if l == 0:
		l +=1

	s0 = "a" * l
	ret.append(s0)
	
	il = 1
	for i in a:
		pivot = letters[il]
		si = ret[-1][:i]
		#print ("{}: {}; pivot: {}".format(il, si, pivot)) # DEBUG
		si += (l - len(si)) * pivot
		if len(si) < i:
			if si[i] == ret[-1][i]:
				il += 1
				if il == 26:
					il = 0

				si = si[:i] + letters[il] + si[i+1:]
		ret.append(si)
		
		il += 1
		if il == 26:
			il = 0
		
	return ret


# Main
t = read_int()
for case in range(t):
	n = read_int()
	a = read_ints()
	sol = solve(a, n)
	for line in sol:
		print (line)
