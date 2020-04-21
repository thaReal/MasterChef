#!/usr/bin/python3

# Codeforces - Round 636
# Problem C - Alternating Subsequence


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, a):
	if a[0] > 0:
		sign = 1
	else:
		sign = -1
		
	sol = []
	choices = [a[0]]
	for elem in a[1:]:
		if elem / sign < 0:
			sol.append(max(choices))
			choices = [elem]
			sign = -1 if sign == 1 else 1
		else:
			choices.append(elem)
	
	sol.append(max(choices))
	
	return sum(sol)
		

# Main
t = read_int()
for case in range(t):
	n = read_int()
	a = read_ints()
	sol = solve(n, a)
	
	print (sol)
