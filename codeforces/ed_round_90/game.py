#!/usr/bin/python3

# Codeforces - Educational Round #90
# Author: frostD
# Problem B - 01 Game


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(s):
	moves = 0
	ms1 = s.split('10') # move set 1
	ms2 = s.split('01') # move set 2
	
	while len(ms1) > 1 or len(ms2) > 1:
		if len(ms1) > len(ms2):
			moves += len(ms1) - 1
			s = ''.join(ms1)
		
		else:
			moves += len(ms2) - 1
			s = ''.join(ms2)
		
		ms1 = s.split('10') # move set 1
		ms2 = s.split('01') # move set 2
		
	if moves % 2 == 1:
		return "DA"
	else:
		return "NET"
	


# Main
t = read_int()
for case in range(t):
	s = input()
	sol = solve(s)
	print (sol)
