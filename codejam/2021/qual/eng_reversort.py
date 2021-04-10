#!/usr/bin/python3
'''
Codejam 2021 Qualification Round
Problem: "Reversort Engineering"
Author: Daniel Ruland
'''

# Utility Functions
def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	
	
# Solution:
def solve(n, c):
	if c < n-1:
		return "IMPOSSIBLE"    
	
	mx = int((((n+1) * ((n+1) - 1)) / 2) - 1)
	if c > mx:
		return "IMPOSSIBLE"
	    
	# subtract min value (1 for each sorted element)
	c -= (n - 1)
	
	ret = [(x+1) for x in range(n)]
	li = 0
	ri = n
	side = 1 # 1 is left, -1 is right
	
	# if value is used reverse, flip side, and decrement cost 
	# both cases - decrese window depending on side
	for i in range(n-1):
		if (n - i - 1) <= c:
			ret = ret[:li] + ret[li:ri][::-1] + ret[ri:]
			side *= -1
			c -= (n - i - 1)
		
		if side == 1:
			li += 1
    		
		else:
			ri -= 1
	
	return ' '.join([str(x) for x in ret])

# Main
T = read_int()
for i in range(T):
    n, c = read_ints()
    sol = solve(n, c)
	
	# Output
    print ("Case #{}: {}".format(i+1, sol))
