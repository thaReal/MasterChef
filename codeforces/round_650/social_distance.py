#!/usr/bin/python3

# Codeforces - Round 650
# Author: frostD
# Problem C - Social Distance


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, k, s):
	if s.count('1') == 0:
		new_tables = 1
		empty_tables = s.count('0')
		new_tables += (empty_tables - 1) // (k + 1)
		return new_tables

	groups = []
	cntr = 0
	for i in range(n):
		if s[i] == '0':
			cntr += 1
		else:
			if cntr != 0:
				groups.append(cntr)
			cntr = 0
			
	if cntr != 0:
		groups.append(cntr)


	new_tables = 0
	for i in range(len(groups)):
		if i == 0 and s[0] == '0':
			new_tables += groups[i] // (k+1)
		elif i == (len(groups) - 1) and s[-1] == '0':
			new_tables += groups[i] // (k+1)
		else:
			new_tables += (groups[i] - k) // (k + 1)
		
	return new_tables


# Main
t = read_int()
for case in range(t):
	n, k = read_ints()
	s = input()
	sol = solve(n, k, s)
	print (sol)
