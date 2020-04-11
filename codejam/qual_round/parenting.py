#!/usr/bin/python3
'''
Codejam 2020 Qualification Round 
Problem: "Parenting Partnering Returns"
Author: Daniel Ruland
'''

# Utilility Functions
def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	
	
def solve(times):
	# Need to maintain original event mapping
	event_dict = dict()
	cntr = 0
	for time in times:
		event_dict[cntr] = time
		cntr += 1
	
	times.sort()
	
	sol0 = ''
	c_end = 0
	j_end = 0
	for t in times:
		ts, te = t
		
		if c_end <= ts:
			c_end = te
			sol0 += 'C'
		
		elif j_end <= ts:
			j_end = te
			sol0 += 'J'
		
		else:
			return 'IMPOSSIBLE'
	
	# map the chronological solution back to the original event order
	sol = ''
	for i in range(len(times)):
		idx = times.index(event_dict[i]) # gives sorted index
		parent = sol0[idx]
		sol += parent
		
		# handle case of two identical, concurrent events
		if times.count(event_dict[i]) == 2:
			parent = 'J' if parent == 'C' else 'J'
			sol0 = sol0[:idx] + parent + sol0[idx+1:]
	
	return sol


# Main
t = read_int()
case = 1
for x in range(t):
	# Solution
	n = read_int()
	times = []
	for i in range(n):
		s, e = read_ints()
		times.append((s, e))
		
	y = solve(times)
	
	# Output
	print ("Case #{}: {}".format(x+1, y))
	case += 1
