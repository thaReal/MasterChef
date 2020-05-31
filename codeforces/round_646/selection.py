#!/usr/bin/python3

# Codeforces - Round 646
# Author: frostD
# Problem A - 


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, x, a):
	odds = 0
	evens = 0
	for i in a:
		if i % 2 == 0:
			evens += 1
		else:
			odds += 1
	#print ("odds: {}, evens: {}".format(odds, evens))
	
	if n == x:
		if sum(a) % 2 == 0:
			return 'NO'
		else:
			return 'YES'
	
	if x % 2 == 1:
		if odds >= 1:
			return 'YES'
		else:
			return 'NO'
	
	else:
		if odds >= 1 and evens >= 1:
			return 'YES'
		else:
			return 'NO'
		


# Main
t = read_int()
for case in range(t):
	n, x = read_ints()
	a = read_ints()
	sol = solve(n, x, a)
	
	print (sol)
