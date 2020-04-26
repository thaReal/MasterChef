#!/usr/bin/python3

# Codeforces - Educational Round 86
# Problem B - Binary Period


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(t):
	lmax = len(t) * 2
	sol = ''
	
	if t.find('0') == -1:
		period = '1'
		
	elif t.find('1') == -1:
		period = '0'

	elif t.find('01') == -1:
		period = '10'
	
	else:
		period = '01'
	
	lp = len(period)
	if lp == 1:
		return len(t) * period
	
	i = 0
	for j in range(len(t)):
		idx = i % 2
		val = period[idx]
		if val != t[j]:
			sol += val
			i += 1
		sol += t[j]
		i += 1
	
	return sol
			
	

# Main
T = read_int()
for case in range(T):
	t = input()
	sol = solve(t)
	
	print (sol)
