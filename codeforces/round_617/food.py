#!/usr/bin/python3

# Codeforces - Round 617 - Practice
# Author: frostD
# Problem B - Food Buying 

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(s):
	ret = 0
	while s >= 10:
		ret += (s//10) * 10
		s = (s//10) + (s%10)
	
	ret += s
	
	return ret		
		
		
	


# Main
t = read_int()
for case in range(t):
	s = read_int()
	sol = solve(s)
	print (sol)
