#!/usr/bin/python3

# Codeforces - Educational Round 85
# Problem A - Level Statistics


# Utilility Functions

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints


def solve(n, stats):
	p0 = stats[0][0]
	c0 = stats[0][1]

	if c0 > p0:
		return 'NO'

	if n == 1:
		return 'YES'	
	
	for i in range(len(stats) - 1):
		p = stats[i+1][0]
		c = stats[i+1][1]
		
		# Neither can go down on a subsequent peek
		if p < p0:
			return 'NO'

		if c < c0:
			return 'NO'
		
		# can never be more clears than plays
		if c > p:
			return 'NO'
		
		# num of new clears can't be more than num of new plays
		if c - c0 > p - p0:
			return 'NO'
		
		p0 = p
		c0 = c
	
	return 'YES'
	
		

# Main
T = read_int()
for case in range(T):
	n = read_int()
	stats = []
	for i in range(n):
		p, c = read_ints()
		stats.append((p, c))
	
	sol = solve(n, stats)
	print (sol)	
	
