#!/usr/bin/python3

# Codeforces - Round 659 - [Virtual Practice]
# Author: frostD
# Problem B - Koa and the Beach (Easy Version) 

'''
This technically would be valid except I overlooked the part that she can also choose
to wait and at this point of the day I'm to tired to try to work that in
'''

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, k, l, d):
	# l = max swimmable depth, k = tide length
	max_depth = max(d)
	idx = d.index(max_depth)
	swim = [0] * n
	
	# do the right half first
	rising = True
	level = 0
	for i in range(idx, n):
		swim[i] = l - d[i] - level
		if rising:
			if level < k:
				level += 1
			else:
				rising = False
				level -= 1
		else:
			if level > 0:
				level -= 1
			else:
				rising = True
				level += 1
	
	# Then the left half
	rising = True
	level = 1
	while idx > 0:
		idx -= 1
		swim[idx] = l - d[idx] - level
		if rising:
			if level < k:
				level += 1
			else:
				rising = False
				level -= 1
		else:
			if level > 0:
				level -= 1
			else:
				rising = True
				level += 1
	
	print (swim) #DEBUG
	if min(swim) >= 0:
		return "Yes"
	
	else:
		return "No"
		


# Main
t = read_int()
for case in range(t):
	n, k, l = read_ints()
	d = read_ints()
	sol = solve(n, k, l, d)
	print (sol)
